from mrjob.job import MRJob
from mrjob.step import MRStep
import re


class NCDC(MRJob):
    invalid_stations = set()
    months = [
        '01', '02', '03', '04', '05', '06',
        '07', '08', '09', '10', '11', '12'
        ]
   
    def steps(self):
        return [
            MRStep(mapper=self.mapper_,
                   combiner=self.combiner_,
                   reducer=self.reducer_1),
            MRStep(reducer=self.reducer_2),
            #MRStep(reducer=self.reducer_),
        ]

    def mapper_(self, _, line):
        if '*' in line:
            data = line.split(' ')
            for month in self.months:
                key = data[0] + data[2][:4] + month
                if data[2][4:6] != month:
                    yield (key, 0)
                else:
                    yield(key, 1)            

    def combiner_(self, key, values):
        yield(key, sum(values))

    def reducer_1(self, key, values):
        yield(key, sum(values))

    def reducer_8(self, key, values):

        for i in values:
            print(key, i)
        yield(None, sum(values))

    def reducer_2(self, key, values):
        for value in values:
            #print(key, value)
            if value < 2:
                self.invalid_stations.add(key[:-2])
                #print(self.invalid_stations)
            return


class Filter(MRJob):
    invalid_stations = NCDC.invalid_stations

    def steps(self):
        return [
            MRStep(mapper=self.mapper_,
                   reducer=self.reducer_),
        ]

    def mapper_(self, _, line):
        if '****' in line:
            data = line.split(' ')
            key = data[0] + data[2][:4]
            print(self.invalid_stations)
            if key in self.invalid_stations:
                yield (None, line)

    def reducer_(self, key, values):
        for value in values:
            yield(value, None)

if __name__ == '__main__':
    NCDC.run()
    Filter.run()


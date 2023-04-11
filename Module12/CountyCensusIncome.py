"""
Student: Dominic Wood
Class: CIS189
CRN: 21906
Module: 12
Topic: 1
Assignment: CSV Import to Class Object
Date: 04/05/2023
"""
import csv

class CountyCensusIncome:

    _rank: int
    _county: str
    _per_capita_income: int
    _median_household_income: int
    _median_family_income: int
    _population: int
    _household_count: int

    def __init__(self, 
                 rank, 
                 county, 
                 per_capita_income, 
                 median_household_income,
                 median_family_income,
                 population,
                 household_count):
        self._rank = rank
        self._county = county
        self._per_capita_income = per_capita_income
        self._median_family_income = median_family_income
        self._median_household_income = median_household_income
        self._population = population
        self._household_count = household_count

    def __str__(self) -> str:
        result = f'State Rank: {self._rank}, '
        result += f'County: {self._county}, '
        result += f'Per Capita Income: ${self._per_capita_income}, '
        result += f'Median Household Income: ${self._median_household_income}, '
        result += f'Population: {self._population}, '
        result += f'Number of Households: {self._household_count}'
        return result
    
    def population_per_household(self):
        return int(self._population.replace(',', ""))/int(self._household_count.replace(',', ""))
    
if __name__ == '__main__':
    counties = dict()
    with open('Iowa 2010 Census Data Population Income.csv') as file:
        reader = csv.reader(file, delimiter=',')

        for line in reader:
            # skip line if first value is not a rank integer
            try:
                int(line[0])
            except ValueError:
                continue
            counties.update({line[1]: CountyCensusIncome(line[0],
                                                   line[1],
                                                   line[2],
                                                   line[3],
                                                   line[4],
                                                   line[5],
                                                   line[6])})
    print("Dallas county population per household: " +
          f"{counties['Dallas'].population_per_household():.02f}")
    
    iowa_pop = 0
    for county in counties:
        iowa_pop += int(counties[county]._population.replace(",",""))
    print(f'Population of Iowa: {iowa_pop:,}')
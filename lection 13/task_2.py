class Country:
    def init(self, name, population):
        self.name = name
        self.population = population

    def add(self, other_country):
        combined_name = f"{self.name} {other_country.name}"
        combined_population = self.population + other_country.population
        return Country(combined_name, combined_population)

# Example usage:
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.population)  # Output: 15000000
print(bosnia_herzegovina.name)  
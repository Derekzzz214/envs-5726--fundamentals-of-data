import datetime
import statistics

class PreySample:
    def __init__(self, full_species_name, delta13c_list, tissue_description, sample_due_utc):
        self.full_species_name = full_species_name
        self.delta13c_list = delta13c_list
        self.tissue_description = tissue_description
        self.sample_due_utc = sample_due_utc

    def get_common_name(self):
        return self.full_species_name.split("(")[0]

    def get_scientific_name(self):
        return self.full_species_name.split("(")[1].split(")")[0]

    def get_average_delta13c(self):
        return statistics.mean(self.delta13c_list)

    def get_tissue_count(self):
        return len(self.tissue_description.split(", "))

    def get_sample_date(self):
        return datetime.datetime.strptime(self.sample_due_utc, "%Y-%m-%dT%H:%M:%SZ")

    def get_discrimination_factor(self, predator_deltal3c: float):
        prey_avg = self.get_average_delta13c()
        return predator_deltal3c - prey_avg

sample1 = PreySample(
    full_species_name = 'Harbor Seal (Phoca vitulina)',
    delta13c_list = [-12.4, -11.3, -10.6, -13.5, -15.8],
    tissue_description = 'Bone collagen, Bone collagen, Muscle, Skin',
    sample_due_utc = '2020-11-16T04:25:03Z',
)

print(sample1.get_common_name())
print(sample1.get_scientific_name())
print(sample1.get_average_delta13c())
print(sample1.get_tissue_count())
print(sample1.get_sample_date())

sample2 = PreySample(
    full_species_name = 'Pacific pomfret (Brama japonica)',
    delta13c_list = [-16.1, -17.8, -19.6, -19.1, -18.0],
    tissue_description = 'Whole animal',
    sample_due_utc = '2020-11-16T05:00:02Z',
)

print(sample2.get_discrimination_factor(predator_deltal3c=-15.5))

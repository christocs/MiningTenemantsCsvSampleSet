import sampleset
import miningTenementTemplate

def main():
    # sampleset.generateSampleSet()
    miningTenementTemplate.fix("tenement_templates_dupes_removed.csv", "tenement_templates_fixed.csv")
    miningTenementTemplate.generateRegex("tenement_templates_fixed.csv", "tenement_templates_regex.csv")

if __name__ == '__main__':
    main()
import sampleset
import miningTenementTemplate
import findtemplates

def main():
    # sampleset.generateSampleSet()
    # miningTenementTemplate.fix("tenement_templates_dupes_removed.csv", "tenement_templates_fixed.csv")
    # miningTenementTemplate.generateRegex("tenement_templates_fixed.csv", "tenement_templates_regex.csv")
    # findtemplates.printNoMatches("Conditions.csv", "tenement_templates_regex.csv")
    findtemplates.dumpUnmatchedRows("Conditions.csv", "tenement_templates_regex.csv", "ConditionsNoRegexMatches.csv")

if __name__ == '__main__':
    main()
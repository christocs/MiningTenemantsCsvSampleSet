import sampleset
import miningTenementTemplate
import findtemplates

def main():
    # sampleset.generateSampleSet()

    # miningTenementTemplate.fix("tenement_templates_dupes_removed.csv", "tenement_templates_fixed.csv")
    # miningTenementTemplate.generateRegex("tenement_templates_fixed.csv", "tenement_templates_regex.csv")
    # miningTenementTemplate.stripDuplicateRegex("tenement_templates_regex.csv",
    #                                            "tenement_templates_regex_no_overlapping_templates.csv")
    # findtemplates.dumpMatchedRows("Conditions.csv", "tenement_templates_regex_no_overlapping_templates.csv", "ConditionsWithRegexMatches.csv")

    findtemplates.dumpMatchedRowsWhichOnlyMatchGreedyRegex("Conditions.csv", "tenement_templates_regex_no_overlapping_templates.csv",
                                  "ConditionsWithRegexMatchesThatOnlySatisfyGreedyRegex.csv")

    # findtemplates.printNoMatches("Conditions.csv", "tenement_templates_regex.csv", "CondText", False)

    # Check templates match against themselves
    # findtemplates.printNoMatches("tenement_templates_regex.csv", "tenement_templates_regex.csv", "Text", True)
    # findtemplates.selfMatchTemplateFile("tenement_templates_regex.csv")
    # findtemplates.selfMatchTemplateFileFindOverlappingTemplates("tenement_templates_regex.csv")
    # findtemplates.dumpUnmatchedRows("Conditions.csv", "tenement_templates_regex.csv", "ConditionsNoRegexMatches.csv")
    # findtemplates.selfMatchTemplateFileFindOverlappingTemplates("tenement_templates_regex.csv")
    # findtemplates.selfMatchTemplateFileFindOverlappingTemplates("tenement_templates_regex_dupes_removed.csv")

if __name__ == '__main__':
    main()
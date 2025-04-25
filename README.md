# Compatibility-Predictor

# Overview
- Uses a weight system to determine compatibility between the team and applicants.  Or if the user has an ideal candidate in mind, they will use that to generate a better compatibilty score.
- If you want favor an attribute of an applicant more (e.g., intelligence, strength), use weights to control how much that attribute will contribute to the final compatibility score of the applicant.
- If you do not want a compatibility score based on the current team, then generate an ideal profile in a JSON file.
- The default scoring will use the team average which will compare the team's average score to the applicant's score.


# Input
- The input should be a JSON file containing an "applicants" array.
- For each applicant, it should include a name and a dictionary of attributes.

# Output
- The output will be a JSON file containing a JSON object with "scoredApplicants", along with the applicants name, and score associated with them.

# How To Run
- Input file will default to input.json if not specified.  If user wishes to specify input file, use command line arguments such as:
*- python3 predictor.py --input-file sample_input.json


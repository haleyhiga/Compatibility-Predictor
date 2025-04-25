import argparse
import json
import sys


'''
If the user decides that a certain attribute is more important, they will increase the weight for that attribute.
Ensure that all the weights sum up to 1.0.
'''
weights = {
    "intelligence": 0.15,
    "strength": 0.1,
    "endurance": 0.25,
    "spicyFoodTolerance": 0.5,
}


'''
Generate Compatibility Score
'''
def get_score(person):
    total = 0
    for attr, weight in weights.items():            # Loop over the key and values in weights
        value = person["attributes"].get(attr, 0)  # Get the value of the attribute for that specific person, if the attribute does not exist, it will default to 0.
        total += weight * (value / 10.0)              # Take the attribute value and divide it by 10, multiply by the weight to get the final score.
    return total


# If the user chooses to use an ideal profile, similar to get_score function, but is based on the ideal profile
def get_ideal_score(ideal_profile):
    total = 0
    for attr, weight in weights.items():
        value = ideal_profile.get(attr, 0)
        total += weight * (value / 10.0)
    return total


# If the user wants to use the team average
def get_team_avg_score(team):
    total = 0
    for person in team:
        total += get_score(person)
    return total / len(team)


# Give applicants compatibility scores
def score_applicants(applicants, base_score):
    results = []
    for applicant in applicants:
        applicant_score = get_score(applicant)  # Get the score of the applicant
        compatibility = round(1 - abs(applicant_score - base_score), 2) # Take the difference between the applicant score and the base score (ensure its between 0 and 1)
        results.append({    # Create our output
            "name": applicant["name"],
            "score": compatibility
        })
    return results



'''
Used to specify input and output files from the command line if the user does not want to use the defaults.
'''
def parse_args(argv):
    parser = argparse.ArgumentParser(description="Run Compatibility Predictor")
    parser.add_argument("--input-file", "-i", default="input.json", help="Specify JSON input file.")
    parser.add_argument("--output-file", "-o", default="output.json", help="Specify JSON output file.")
    parser.add_argument("--ideal-profile", "-p", help="Optional ideal profile JSON file")
    return parser.parse_args(argv[1:])


def main(argv):
    args = parse_args(argv)

    with open(args.input_file, "r") as f:
        data = json.load(f)

    applicants = data.get("applicants")
    team = data.get("team")

    if args.ideal_profile:
        with open(args.ideal_profile, "r") as pf:
            ideal = json.load(pf)
        base_score = get_ideal_score(ideal)
        print("Using ideal profile to generate compatibility scores.")
    else:
        base_score = get_team_avg_score(team)
        print("Using team average to generate compatibility scores.")

    result = {"scoredApplicants": score_applicants(applicants, base_score)}

    with open(args.output_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Output saved to: {args.output_file}")


if __name__ == "__main__":
    main(sys.argv)

  

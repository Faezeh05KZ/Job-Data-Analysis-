import pandas as pd

def analyze_jobs(csv_file, skill):
    try:
        df = pd.read_csv(csv_file)

    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
        return
    
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    print("Columns in CSV:", df.columns.tolist())

    if 'Skills' not in df.columns:
        print("Error: The 'Skills' column is missing in the CSV file!")
        return

    print("First few rows of data:\n", df.head())

    skill_count = df[df['Skills'].str.contains(skill, case=False, na=False)].shape[0]

    print(f"Number of jobs related to the skill '{skill}': {skill_count}")

    with open('job_analysis_output.txt', 'w', encoding='utf-8') as f:
        f.write(f"Number of jobs related to the skill '{skill}': {skill_count}\n")

if __name__ == "__main__":
    analyze_jobs('jobs.csv', 'Python')
import os
from email_parser import parse_eml
from analyzer import analyze_email
from utils import get_timestamped_filename, save_json_report

def main():
    # Folder containing multiple .eml files
    eml_folder = r"D:\Cyber Internship\APADS\email_detector\test_emails"
    reports_folder = r"D:\Cyber Internship\APADS\dashboard\reports"

    if not os.path.exists(eml_folder):
        print("Folder not found! Make sure the path is correct.")
        return

    # Create reports folder if it doesn't exist
    os.makedirs(reports_folder, exist_ok=True)

    for file_name in os.listdir(eml_folder):
        if file_name.endswith(".eml"):
            eml_file = os.path.join(eml_folder, file_name)
            print(f"\nProcessing file: {eml_file}")

            try:
                data = parse_eml(eml_file)
                report = analyze_email(data)

                # Generate a timestamped filename for each report
                filename = get_timestamped_filename(folder=reports_folder)
                save_json_report(report, filename)

                print(f"Report saved to: {filename}")
            except Exception as e:
                print(f"Error processing {eml_file}: {e}")

if __name__ == "__main__":
    main()

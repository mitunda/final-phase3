# Baby Records Management CLI
## Overview
- The Baby Records Management CLI is a command-line application that allows healthcare professionals to manage baby records. It provides features for adding new baby records, viewing baby records, updating baby records, and deleting baby records.
## Installation
- To use this CLI tool, you'll need Python and SQLite installed on your system.
1. Clone the repository:

   ```sh
   git clone https://github.com/mitunda/final-phase3.git
   cd final-phase3
- Install the required dependencies:
## Usage
### Adding a New Baby Record
- To add a new baby record, run the following command:
    - python cli.py add-baby --baby_name "Baby Name" --baby_weight 3.2 --birth_date "2023-09-07" --sickness_details "No known sickness"
### Viewing Baby Records
- To view all baby records, use the following command:
    - python cli.py view-babies
- To view a specific baby record by ID, use:
    - python cli.py view-baby --baby_id 1
### Updating Baby Records (Not Implemented Yet)
- (Instructions for updating baby records can be added here once implemented.)
### Deleting Baby Records
- To delete a baby record by ID, use the following command:
    - python cli.py delete-baby --baby_id 1
# Contact
- Author: Peter Mitunda
- Email: peterbrian28@gmail.com
- GitHub: https://github.com/mitunda
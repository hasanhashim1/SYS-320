# By Hasan Hashim
# Adding all of the libary we want for this script 
import argparse
import csv
import os
import sys
import yaml


# Creatting a function that parsing the arguments for our program
def parse_args():
    # Here we are starting the parsering proces
    parser = argparse.ArgumentParser(
        description="Hello we are Here to Parses Forensic Toolkit Collections from a directory",
        epilog="Developed by Hasan Hashim, 10192022",
    )

    # Here adding argument for the directory of the logs to parse
    parser.add_argument( "-d", "--directory", required=True, help="Add the directory that contains the collections files.",)  
    # Here adding argument to search logs
    parser.add_argument( "-s", "--search", required=True, help="Here put the name of YAML document containing search strings.",)

     #Parse arguments
    args = parser.parse_args()

    # Now we need to check if the dir argument is a directory
    if not os.path.isdir(args.directory):
        print(f"Invalid directory => {args.directory}")
        sys.exit()

    # Return parsed args
    return args


# Going to the directory and append the contents of each file to a list
def walk_csv_dir(rootdir):
    f_list = []

    # Now we crawl through the provided directory
    for root, _, filenames in os.walk(rootdir):
        for f in filenames:
            f_list.append(root + "/" + f)

    # we need to list to save file contents
    csv_contents = []

    # Going through the list in the files
    for file in f_list:
        # Here we are oping the file
        with open(file, "r", encoding="utf-8") as f:
            # Here we are listing ID, arguments, hostname, name, path, pid, username
            reader = csv.DictReader(f)
            for row in reader:
                csv_contents.append(row)
    # Returning the resulte
    return csv_contents


# Her I'm load all of my yaml documents from search terms
def load_yaml(file, document):

    # Here I'm adding all our rules to a list to by pass dictionary key/value names
    with open(file, "r", encoding="utf-8") as f:
        yaml_rules = list(yaml.safe_load_all(f))

    # Going through the list of rules and select desired rules
    for rule in yaml_rules:
        if document in rule.keys():
            return rule[document]

    # Here if a file did not open the proram will say document does not exist
    print(f"Error: Specified document {document} does not exist in search terms")
    sys.exit()

# Here are our main function that has the rest of the program
def main():
    args = parse_args()
    contents = walk_csv_dir(args.directory)
    yaml_data = load_yaml("searchTerms.yaml", args.search)
    # Goin through each line in the file
    for line in contents:
        # Going through each search term in the yaml file
        for term in yaml_data.get("search"):
            # Now we are check if the search term is in the line
            if term in line.get("arguments"):
                # Here we are output the line's information
                print (
                    "Type: {} | {} | {} | {} | {} | {} | {}".format(
                        yaml_data["type"],
                        line["arguments"],
                        line["hostname"],
                        line["name"],
                        line["path"],
                        line["pid"],
                        line["username"],
                    )
                )


if __name__ == "__main__":
    main()
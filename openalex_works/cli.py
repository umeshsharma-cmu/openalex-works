import argparse
from openalex_works.works import OpenAlexWorks


def main():
    parser = argparse.ArgumentParser(
        description="Get RIS or bibtex for a DOI from OpenAlex Works"
    )
    parser.add_argument("doi", help="DOI of the publication")
    parser.add_argument(
        "format", choices=["ris", "bibtex"], help="Output format (ris or bibtex)"
    )

    args = parser.parse_args()

    work = OpenAlexWorks(args.doi)
    if args.format == "ris":
        print(work.get_ris())
    else:
        print(work.get_bibtex())


if __name__ == "__main__":
    main()

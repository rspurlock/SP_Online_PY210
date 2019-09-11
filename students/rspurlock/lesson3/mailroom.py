#!/usr/bin/env python3

import sys

# Global variables
donorDb = [("Jeff Bezos",       [4.37]),
           ("Mark Zuckerberg",  [4.11, 12.53, 167.99]),
           ("Jensen Huang",     [1213.45, 4664.33]),
           ("Robert Swan",      [10156.00, 25321.17]),
           ("Lisa Su",          [1.23, 4.56, 7.89, 17.13, 23.31]),
           ("Satya Nadella",    [8.00, 10.00]),
           ("Bill Gates",       [423178.99, 576821.01])
          ]

mailPrompt = "\n".join(("Welcome to the mailroom!",
                        "Please choose one of the following:",
                        "1 - Send Thank You",
                        "2 - Create a Report",
                        "3 - Exit",
                        ">>> "))
donorPrompt = "\n".join(("Please enter donor full name",
                        "or list for current donor list",
                        ">>> "))


def sortName(donorEntry):
    """
    Sort Function to return donor name for sorting donor list (Last Name, First Name)

    Positional Parameters
    :param donorEntry:  Donor database entry to return name for sorting

    :return:            Returns donor last name, first name for sorting
    """
    # Split the donor entry name
    donorName = donorEntry[0].split(" ")

    # Return the donor last name, first name
    return donorName[1] + ", " + donorName[0]


def sortDonations(donorEntry):
    """
    Sort Function to return donor donation total for sorting donor list (by donations)

    Positional Parameters
    :param donorEntry:  Donor database entry to return donation total for sorting

    :return:            Returns donor donation total for sorting
    """
    # Return the donor donation total
    return sum(donorEntry[1])


def donorList():
    """
    Function to display the current donor list (sorted)
    """
    # Sort the donor database by name (last, first)
    sortedDonors = sorted(donorDb, key=sortName)

    # Display the sorted donor list to the user
    for donor in sortedDonors:
        print(donor[0])


def sendThankYou():
    """
    Send Donor Thank You Function (Prompts user for donor name and donation amount)
    """
    # Loop in case user wants current donor list
    while(True):
        # Prompt user for donor name
        donorName = input(donorPrompt)

        # Check to see if user requested current donor list or exit (No name)
        if (donorName.lower() == 'list'):
            donorList()
        elif (len(donorName) == 0):
            break
        else:
            # Check to see if this name is in the donor database
            donorEntry = None
            for donorIndex in range(len(donorDb)):
                if (donorDb[donorIndex][0] == donorName):
                    donorEntry = donorDb[donorIndex]
                    break
            # Check to see if we did not find a matching donor
            if (donorEntry == None):
                # Create and add this donor to the database
                donorEntry = (donorName, [])
                donorDb.append(donorEntry)

            # Prompt user for a donation amount
            donation = float(input("Please enter a donation amount: "))

            # Add this donation to the donor entry
            donorEntry[1].append(donation)

            # Setup variables for generating thank you email
            donorName = donorEntry[0]
            donations = sum(donorEntry[1])

            # Create a donation type based on the donation value
            if (donation < 10.00):
                donationType = " "
            elif (donation < 100.00):
                donationType = " gracious "
            elif (donation < 1000.00):
                donationType = " generous "
            elif (donation < 10000.00):
                donationType = " very generous "
            else:
                donationType = " extremely generous "

            # Create a donations type based on the donations value
            if (donations < 100.00):
                donationsType = " "
            elif (donations < 1000.00):
                donationsType = " a wonderful "
            elif (donations < 10000.00):
                donationsType = " a fantastic "
            elif (donations < 100000.00):
                donationsType = " a stupendous "
            else:
                donationsType = " a staggering "

            # Build thank you email for this donor
            thankYou = "\n".join((f'Dear {donorName},',
                                  f'',
                                  f'Thank you for your recent{donationType}donation of ${donation:,.2f}',
                                  f'This donation brings your donation total to{donationsType}${donations:,.2f}!',
                                  f'',
                                  f'Once again, thanks for your generosity!'
                                ))

            print(thankYou)

            break


def createReport():
    """
    Create report for the current donor database
    """
    # Sort the donor database by donations (donation total)
    sortedDonors = sorted(donorDb, key=sortDonations, reverse=True)

    # Display the report header
    print('Donor Name                |  Total Given  | Num Gifts |  Average Gift ')
    print('----------------------------------------------------------------------')

    # Display the sorted donor list to the user
    for donor in sortedDonors:
        print(f'{donor[0]:26} ' + "{:>15}".format(f'${sum(donor[1]):,.2f} ') + f'{len(donor[1]):^11d} ' + "{:>15}".format(f'${sum(donor[1])/len(donor[1]):,.2f}'))


def main():
    """
    Main mailroom entry point
    """
    response = 0

    # Loop forever (Until the user selects exit)
    while (True):
        # Prompt the user for an option
        response = input(mailPrompt)
        # Check the user response
        if (int(response) == 1):
            # Send a donor thank you
            sendThankYou()
        elif (int(response) == 2):
            # Create a report for the user
            createReport()
        elif (int(response) == 3):
            # Exit the mailroom
            sys.exit()
        else:
            print("Invalid option selected!")

# Guard against running this code if imported
if __name__ == "__main__":
    main()

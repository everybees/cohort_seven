number_of_point_team_is_ahead_with = float(input("Enter number of point team is ahead with: "))


def calculate_number_of_point(calculate_number_of_points):
    calculate_number_of_points = float(number_of_point_team_is_ahead_with) - 3


def verify_team_with_the_ball(calculate_number_of_points):
    which_team_has_the_ball = input("Enter YES if team A has the ball and No if team B has the ball: ")
    if which_team_has_the_ball == "yes":
        calculate_number_of_points + 0.5
    else:
        calculate_number_of_points - 0.5





def verify_for_negative_input():
    calculate_number_of_point()
    if calculate_number_of_points < 0:
        calculate_number_of_points = 0

def calculating_for_square_of_number():
    square_of_number = square_of_number ** 2
    number_seconds_left = int(input("Enter number of second needed for the match to finish : "))
    if square_of_number > number_seconds_left:
        print("the lead is safe")
    else:
        print("the lead is not safe.")

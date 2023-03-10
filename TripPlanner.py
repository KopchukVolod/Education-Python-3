# TripPlanner-V1.0.
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)
trip_planner_welcome("Volodymyr")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(2.8)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin + " And you are traveling to " + destination + " You will be traveling by " +  mode_of_transport + " It will take approximately "  + str(estimated_time) + " hours")
destination_setup("Zhytomyr", "Kyiv", estimate)

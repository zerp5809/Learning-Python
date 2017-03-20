__author__ = 'Shane Yang'
class MadStoryMaker():
    def makeStory(activity, location, bodyPart, mood):
        if activity[0].lower() == "a" or activity[0].lower() == "e" or activity[0].lower() == "i" or activity[0].lower() == "o" or activity[0].lower() == "u":
            msg = "Steve went for an "
        else:
            msg = "Steve went for a "
        msg += activity
        msg += ". During his "
        msg += activity
        msg += " he hurt his "
        msg += bodyPart
        msg += ". Steve was "
        msg += mood
        msg += ". He went home to sleep."
        print(msg)

    print("Hello I am the Mad Libs Story maker.")
    activity = raw_input("Please enter an activity: ")
    location = raw_input("Please enter a location: ")
    bodyPart = raw_input("Please enter the name of a body part: ")
    mood = raw_input("Please enter a mood: ")
    makeStory(activity, location, bodyPart, mood)

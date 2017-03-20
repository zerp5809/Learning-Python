__author__ = 'Shane Yang'
class MadStoryMaker():
    def makeStory(activity, location, bodyPart, mood):
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

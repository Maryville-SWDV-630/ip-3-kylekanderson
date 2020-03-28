# SWDV-630: Object-Oriented Coding
# Kyle Anderson
# Week 3 Assignment

##################################
# INSTRUCTIONS
##################################
# Consider the following code:

class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print (self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")

    def __str__(self):
        return "This charm summons an object to the caster, potentially over a significant distance"

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

    def get_description(self):
        return "Causes the victim to become confused and befuddled."


def study_spell(spell):
    print (spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())

# NOTE: code has been updated for python 3 compatibility

# Answer the following questions:

# 1. What are the parent and child classes here?
# ANSWER: The parent class is Spell and the child classes are Accio and Confundo.

# 2. What are the base and sub-classes?
# ANSWER: The base class is Spell and the sub-classes are Accio and Confundo.

# 3. What is the output from this code?   Try without running if you can
# ANSWER:
# Accio
# Summoning Charm Accio
# No description
# Confundus Charm Confundo
# Causes the victim to become confused and befuddled.

# 4. When study_spell(Confundo()) executes...what get_description method gets called and why?
# ANSWER: When study_spell(Confundo()) executes, it instantiates a Confundo object, then in the study_spell function, it attempts to pretty print the Confundo object. Because the Confundo class does not contain a defined __str__ method, it uses the __str__ method inherited from the parent Spell class. That __str__ method calls self.get_description(). In this case, self refers to the Confundo object, so the get_description method of the Confundo object is called.

# 5. The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? Write down the code that we need to add and/or change.
# ANSWER: To do this, we simply need to implement an __str__ method in the Accio class that returns the string listed above. This will override the __str__ method of the parent class and instead pretty print the string listed above when the print function is called on an Accio object.
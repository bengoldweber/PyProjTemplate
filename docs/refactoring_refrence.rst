- When to refactor
    - First time: just get it done
    - Second time: cringe but do the same thing anyway
    - Third: refactor

    - If adding a feature. Refactoring helps you understand others code
    - Refactoring helps find bugs, since clean code makes it harder for bugs to hide


    Sometimes its worth re-writing code. But when you do - you should already have plently of tests. Otherwise itll end up being youve wasted a bunch of time refactoring.

    Dont mix new features with old.

    All existing tests must pass after refactoring.
        if a test failed. There are two reasons
        - You introduced an error while refacotoring
        - the test were too low level. EX: testing private methods.
            -If this is the case. The test are to blame and should be re-written themselves.

SMELLS

- bloaters: code, methods and classes that have grown to gargauntuan proportions
- OOP abusers: incompleate or incorrect oop principle usage
- Change Preventers: when you try to change something in one place, you also have to change it in many
- Dispensables: pointless and un-nessesary code. Whos removal would make code cleaner
- Couplers: Anything that contributes to excessive coupling.


Bloaters:

    - Long method: Method has too many lines (>10)
    - Large class: contains many fields, methods or lines of code
    - Primative Obsession:
        - Use of primatives instead of small objs
        - Use of constants for info. EX: user_admin_role = 1
        - Use of str constants as field names for use in data arrays
    - Long Params: >3 parameters for a method.
    - Data Clumps: Diff parts of the code contain identical groups of vars. EX: params to conenct to a DB.
        -These should be turned into their own class.

LONG CLASS:
    - Extract a class, subclass or interface

LONG PARAM LIST

- if some params are results of method calls of another obj. USE: Replace Param with Method call.
- Instead of passoing a group of data recieved from another object as a param. Pass the object itself to the method. USING: Preserve Whole Object
- if params are coming from diff sources. pass as a single param as USING: Introduce Parameter Object


import datetime
import random

# there is a README file for this project.
def short_form(idx, *names, **addons): # idx is to return every nth character of a word, *names is the same as *args, which is to accept any no. of arguments
    final = ""
    try:
        for name in names:
            final += name[idx]

        for keys in addons: # for key in dictionary addons...
            if keys == 'prefix': # if the key is 'prefix'
                final = addons[keys] + final # prepend add-on to final
            elif keys == 'suffix':
                final += addons[keys] # append add-on to final
            else:
                print("You\'re bad at typing, aren\'t you?")

    except TypeError as e: # if the user provides an integer instead of a string or smth like that
        print('Wrong data type: ', e)

    except IndexError as e: # if user puts idx as 6 and one of the names as "error" then since the 7th character does not exist it'll throw an error
        print('Indexing issue: ', e)

    except Exception as e:
        print('ERROR: ', e)

    else:
        return final

    finally:
        print("You passed this stage at least.")

strength = {'name' : 10, 'surname' : 20, 'nickname' : 30, 'alias' : 40, 'aka': 50}

def name_strength(**fullname): # **fullname is the same as **kwargs which basically makes a dictionary
    result = 0
    try: 
        for key, value in fullname.items(): # gets interpreted as a dictionary in the "fullname" dictionary
            result += strength[key]*len(value) # for each key, a value is looked up in the dictionary. it then calculates the length of the value given by user, multiplies the strength and length of value and adds it to result
    except KeyError as e:
        print("Too many fields: ", e)
    else:
        return result

def validate(**prelimdata):
    try:
        assert prelimdata['sc'] != None # to ensure key 'sc' data type is not None
        assert prelimdata['ns'] != None
    except KeyError as e:
        print("Validation failed: ", e)
    except AssertionError:
        print("Validation failed: one of the earlier steps failed")
    else:
        print("Working...")
        print("Sending for deeper validation...")
        print("Opening connection to a remote server...")

        try:
            deep_validate(prelimdata)
        except ValueError:
            print("Error, validation failed")
        else: 
            print("Validation successful")
        finally: 
            print("Closing connection to a remote server...")

def deep_validate(prelimdata):
    print(prelimdata)

    now = datetime.datetime.now()
    luck = (now.hour + now.minute + now.second) % 100 # minutes + seconds + hours mod 100
    print(f'Luck --> {luck}')

    threshold_ns = random.randint(1, 200) + luck # random no. b/w 1 and 200 + luck
    threshold_sc = random.randint(10, 20) + luck % 10 # random no. b/w 10 and 20 + luck mod 100 for variability
    print(f'Thresholds --> Name Strength: {threshold_ns}, Short Code Length: {threshold_sc}')

    if prelimdata['ns'] > threshold_ns or len(prelimdata['sc']) > threshold_sc: # if it's earlier in the day then luck will add up to a smaller number, leading to a failure, but if it's late at night then luck will add up to a bigger number leading to higher rates of success
        raise ValueError
    else:
        print("Success!")

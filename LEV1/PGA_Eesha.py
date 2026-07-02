import time
import random

print("🧪 Grumpy PI’s Virtual Assistant: Lab Request Line")

# Q1: Identity check
name = input("Assistant: Who are you? (Full name, not a nickname, not a vibe)\n> ")
if len(name.split()) < 2:
    print("Assistant: One name? What are you, a celebrity? Try again with both names next time.")
else:
    print(f"Assistant: '{name.title()}', fine. You exist. Let’s proceed, unfortunately.")

# Q2: Purpose (Multiple Choice)
print("\nAssistant: Why are you bothering the PI *this time*? Pick ONE. Don't overthink it.")
print("a) Pipette is broken\nb) Need the microscope\nc) I forgot something again\nd) I just like disturbing people")
purpose = input("> ").lower()

# Purpose A
if purpose == "a":
    print("Assistant: Of course. It’s always the pipettes. Handle them like glass next time. Oh wait — they are.")

    print("\nAssistant: What happened to the pipette?")
    print("a) It cracked mid-transfer\nb) The spring popped out\nc) It’s leaking like a faucet\nd) I dropped it. Again.")
    pip_just = input("> ").lower()

    if pip_just == "a":
        print("Assistant: Mid-transfer failure? Tragic. But expected from you.")
    elif pip_just == "b":
        print("Assistant: Did you disassemble it for *fun* again? This is a lab, not LEGO hour.")
    elif pip_just == "c":
        print("Assistant: Wonderful. Now we need a biohazard warning and a mop.")
    elif pip_just == "d":
        print("Assistant: At this point we should just tether the pipette to your hand.")
    else:
        print("Assistant: You can’t even pick a letter. I’m filing a report.")

# Purpose B
elif purpose == "b":
    print("Assistant: Microscopes aren’t even in this building. But sure, wander around.")

    print("\nAssistant: What’s the *real* reason you need the microscope?")
    print("a) You didn’t book it in time\nb) Someone is hogging it\nc) You broke a slide mid-exam\nd) You just want to look at something pretty")
    micro_just = input("> ").lower()

    if micro_just == "a":
        print("Assistant: Shocker. You forgot to book again. A calendar might help.")
    elif micro_just == "b":
        print("Assistant: Let me guess — that one guy who *lives* in the imaging room?")
    elif micro_just == "c":
        print("Assistant: Nice. That's the 3rd broken cover slip this week. Were you stabbing it?")
    elif micro_just == "d":
        print("Assistant: It’s not a kaleidoscope. Take your art therapy elsewhere.")
    else:
        print("Assistant: Invalid input. Eyesight AND memory issues?")

# Purpose C
elif purpose == "c":
    print("Assistant: Shocking. A forgetful scientist. We’ve never seen that before 🙄.")

    print("\nAssistant: What *exactly* did you forget this time?")
    print("a) Antibody for Western blot\nb) Loading dye for gel\nc) The entire sample\nd) Everything. Literally.")
    forget_just = input("> ").lower()

    if forget_just == "a":
        print("Assistant: The primary antibody? The ONE job. Truly inspirational.")
    elif forget_just == "b":
        print("Assistant: No loading dye? That DNA's swimming blind now.")
    elif forget_just == "c":
        print("Assistant: You came to load an empty well. A+ in imagination.")
    elif forget_just == "d":
        print("Assistant: Brave of you to even admit that. Therapy is downstairs.")
    else:
        print("Assistant: Unacceptable. You forgot the options too, apparently.")

# Purpose D
elif purpose == "d":
    print("Assistant: Thanks for the honesty. You still get nothing.")

    print("\nAssistant: What exactly is your goal here?")
    print("a) Start drama in the lab\nb) See if anyone notices\nc) Steal office snacks\nd) No reason, I just enjoy this")
    troll_just = input("> ").lower()

    if troll_just == "a":
        print("Assistant: Chaos is a ladder. You're just climbing the wrong one.")
    elif troll_just == "b":
        print("Assistant: Spoiler: No one noticed. Still don’t.")
    elif troll_just == "c":
        print("Assistant: The snacks are for people with grants. Go earn one.")
    elif troll_just == "d":
        print("Assistant: Peak honesty. Zero contribution. Impressive.")
    else:
        print("Assistant: Invalid trolling. Go practice and come back.")

else:
    print("Assistant: You can't follow basic instructions. I’m lowering the lab IQ just by talking to you.")

# Palindrome check
pal = input("\nAssistant: What’s today’s secret code? It better be a palindrome. (Just for fun... allegedly.)\n> ").lower()
if pal == pal[::-1] and pal != "":
    print("Assistant: Hah. Respect. A palindrome. Rare brain activity detected.")
else:
    print("Assistant: Not a palindrome. Just like your research, it goes nowhere in both directions.")

# Appointment Slot
print("\nAssistant: Against my better judgment, you may request a time slot with the PI.")
slots = ["Mon 9:00 AM", "Tue 11:30 AM", "Wed 3:15 PM", "Thu 1:00 PM", "Fri 10:00 AM"]
random.shuffle(slots)

print("\nHere’s what’s left. Don’t act surprised:")
for i, slot in enumerate(slots):
    print(f"{i+1}. {slot}")

choice = input("\nPick a slot number. One shot.\n> ").strip()
if choice.isdigit():
    num = int(choice)
    if 1 <= num <= len(slots):
        print(f"Assistant: Noted. You're booked for {slots[num - 1]}. Try not to be late *again*.")
    else:
        print("Assistant: That’s not even on the list. Why waste my time?")
else:
    print("Assistant: I said a number. Do you need pipettes or a basic reading class?")

# Time response
start = time.time()
_ = input("\nQuick! Type: 'I solemnly swear to treat the pipettes with care' and press Enter:\n> ")
end = time.time()
reaction = round(end - start, 2)
print(f"Assistant: {reaction} seconds. Not terrible. For a human.")

# Final message
print("\n🧪 Assistant: Your request has been logged. If it were up to me, you’d be denied.")
print("Come back *only* if something explodes — and even then, bring snacks.")

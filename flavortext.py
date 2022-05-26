from random import randrange

constructiveVerbs = ["Aligning", "Building", "Calibrating", "Instancing", "Configuring", "Snorting", "Microwaving", "Tweaking", "Wrangling", "Hacking", "Pwning", "Booting", "Allocating", "Binding", "Revving", "Polishing", "Fabricating", "Pinging",
                     "Refactoring", "Loading", "Quantifying", "Assembling", "Distilling", "Baking", "Receiving", "Unlocking", "Compiling", "Pressurizing", "Chooching", "Making", "Engaging", "Decrypting", "Synthesizing", "Predicting", "Analyzing",
                     "Dispensing", "Firing", "Inserting", "Aligning", "Encouraging", "Extruding", "Accessing", "Sharpening", "Enhancing", "Cranking", "Stacking", "Crafting", "Rendering", "Mounting", "Generating", "Implementing", "Downloading",
                     "Constructing", "Wow! Amazing", "Moistening", "Customizing", "Compensating", "Buffering", "Transferring", "Inducting", "Emitting", "Unzipping", "Squirting", "Feeding", "Buying", "Sparking", "Implanting", "Triangulating",
                     "Injecting", "Linking", "Brewing", "Processing", "Deploying", "Tuning", "Attaching", "Training", "Ignoring", "Tapping", "Reloading", "Simulating", "Fluffing", "Filling", "Sorting", "Updating", "Upgrading", "Priming", "Tracing",
                     "Inflating", "Wangjangling", "Charging", "Cracking", "Ignoring", "Activating", "Pimping", "Collecting", "Approaching", "Approving", "Sampling", "Energizing", "Stuff"]

destructiveVerbs = ["Deallocating", "Trashing", "Unplugging", "Revoking", "Forgetting", "Discarding", "Dropping", "Holstering", "Shredding", "Jettisoning", "Dissolving", "Liquidating", "Releasing", "Collimating", "Ejecting", "Ditching", "Leaking",
                    "Selling", "Banishing", "Dereferencing", "Sacrificing", "Desoldering", "Destructing", "Decompiling", "Blowing", "Disengaging", "Digesting", "Smashing", "Encrypting", "Crashing", "Locking", "Purging", "Regretting", "Rewinding",
                    "Freeing", "Deleting", "Closing", "Retracting", "Collapsing", "Liquefying", "Derezzing", "Stowing", "Archiving", "Suspending", "Suppressing", "Cleaning", "Squashing", "Securing", "Withdrawing", "Dumping", "Obfuscating", "Breaking",
                    "Scrubbing", "Abandoning", "Flattening", "Stashing", "Finishing", "Evacuating", "Scrambling", "Recycling", "Crushing", "Zipping", "Unloading", "Disconnecting", "Loosening", "Containing", "Debating", "Detaching", "Neutralizing",  
                    "Salvaging", "Emptying", "Hiding", "Disarming", "Pickling", "Disregarding", "Yeeting", "Scrapping", "Deflating", "Discharging", "Deactivating", "Sterilizing", "Relieving", "Nuking", "Degaussing", "Dismissing", "Draining", "Rejecting",
                    "Nerfing", "Paying", "Returning", "Unsticking", "Splitting", "Cancelling", "Shaming", "Embezzling", "Flinging", "Regretting", "Halting", "Arresting", "Bury"]

nouns = ["content", "your mom", "the shmoo", "API", "the BJT man", "aesthetics", "backstory", "tactics", "bugs", "sauce", "warp drive", "data", "the funk", "AI", "crystals", "spaghetti", "fluxgate",
         "electrons", "loud noises", "wires", "bytecode", "the truth", "magic", "hot lava", "bits", "Brad", "Teensy", "sensors", "photons", "signal", "the planet", "password", "chips", "circuits",
         "privacy", "synergy", "widgets", "love", "packets", "reality", "lasers", "protocols", "voltage", "registers", "puns", "dogecoins", "kittens", "magic smoke", "plot device", "the core",  "dank memes",
         "subroutines", "radiation", "steam", "trousers", "beer", "protocol", "one-liners", "the Gibson", "software", "a fat one", "holograms", "magnets", "inductors", "resistors", "capacitors", "viewers",
         "subscribers", "sausage", "my wife", "drama", "the future", "vectors", "the clowns", "a Palm Pilot", "5G implant", "monkeys", "breadboard", "Patreon", "money", "the Internet", "fluids", "the impostor",
         "beats", "dopamine", "fedora", "neural net", "comments", "ports", "you. Yes you", "mixtape", "[REDACTED]", "hot tub", "paperwork", "Nerf", "cyber-doobie", "the 1%", "the Matrix", "variables", "IP address"]

def flavortext():
    if randrange(0,2) == 0: l = constructiveVerbs; else: l  = destructiveVerbs
    r,n = randrange(0,len(l)+1), randrange(0,len(nouns)+1)
    return f"{l[r]} {nouns[n]}..."

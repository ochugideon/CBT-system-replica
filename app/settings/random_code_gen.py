import random

NOUNS = [
    "anchor", "apple", "apron", "arch", "armor", "arrow", "artist", "atom", "author", "avocado",
    "badge", "balcony", "banana", "banner", "barrel", "beacon", "beacon", "blanket", "board", "boat",
    "book", "bottle", "boulder", "bracket", "branch", "bridge", "bronze", "broom", "bucket", "buffer",
    "bullet", "button", "cabin", "cable", "cactus", "canyon", "canvas", "captain", "castle", "cavern",
    "ceiling", "cell", "center", "chain", "chair", "chalk", "channel", "chapel", "charm", "chart",
    "cheese", "cherry", "chest", "chimney", "circle", "citrus", "clay", "cliff", "cloak", "clock",
    "cloud", "clover", "column", "comet", "compass", "copper", "coral", "corner", "cottage", "crater",
    "crayon", "creek", "crown", "crystal", "cube", "curtain", "cushion", "dagger", "desert", "diamond",
    "dipper", "dock", "domain", "dragon", "drawer", "engine", "falcon", "feather", "fender", "field",
    "filter", "finger", "flame", "flask", "flute", "forest", "fountain", "frame", "furnace", "galaxy",
    "garden", "garland", "gate", "glacier", "globe", "goblet", "gong", "grain", "granite", "groove",
    "hammer", "harbor", "helmet", "hill", "hollow", "horizon", "horn", "island", "jacket", "jungle",
    "kettle", "key", "kingdom", "ladder", "lantern", "lattice", "leaf", "ledge", "lens", "lever",
    "library", "lightning", "lizard", "lock", "locket", "magnet", "maple", "marble", "matrix", "meadow",
    "medal", "melon", "memory", "mirror", "monument", "moss", "mountain", "needle", "nest", "net",
    "network", "ocean", "orbit", "orchard", "oriel", "palace", "palette", "paper", "parchment", "passage",
    "pebble", "pedal", "pendant", "pepper", "phantom", "pillar", "pillow", "pilot", "pinnacle", "piston",
    "planet", "plate", "pocket", "podium", "portal", "poster", "potion", "prism", "pulley", "pyramid",
    "quartz", "quiver", "radar", "radius", "railway", "raft", "ribbon", "ridge", "river", "rocket",
    "rod", "rooster", "saddle", "sail", "sandal", "satellite", "scalar", "scale", "scepter", "scholar",
    "scroll", "sculpture", "shadow", "shield", "ship", "shuttle", "signal", "silhouette", "silver", "sketch"
]

ADJECTIVES = [
    "abundant", "ancient", "amber", "arcane", "aromatic", "astral", "atomic", "autumn", "azure", "bare",
    "bitter", "blazing", "bleak", "blissful", "bold", "brass", "brave", "breezy", "bright", "brilliant",
    "brittle", "bronze", "brown", "bubbly", "busy", "calm", "candid", "casual", "central", "certain",
    "chilly", "classic", "clean", "clear", "clever", "cloudy", "coastal", "cold", "compact", "complex",
    "cool", "copper", "cosmic", "cozy", "crisp", "critical", "crucial", "crystal", "curious", "damp",
    "daring", "dark", "dazzling", "deep", "dense", "delicate", "digital", "distant", "diverse", "divine",
    "dormant", "dramatic", "dry", "dusty", "dynamic", "eager", "early", "earnest", "earthy", "eccentric",
    "elastic", "electric", "elegant", "elusive", "emerald", "eminent", "endless", "epic", "equal", "eternal",
    "exotic", "faint", "fair", "famous", "fast", "fearless", "fertile", "fierce", "fine", "firm",
    "flawless", "fleet", "flexible", "flowing", "fluent", "fluffy", "fluid", "flying", "focal", "fond",
    "fragile", "fragrant", "free", "fresh", "frosty", "frozen", "gentle", "giant", "gilded", "glacial",
    "glad", "glass", "glowing", "golden", "graceful", "grand", "granite", "grave", "great", "green",
    "grim", "hardy", "harmonic", "harsh", "hasty", "heavy", "hidden", "hollow", "honest", "humble",
    "hushed", "hyper", "icy", "ideal", "idle", "illusive", "immense", "infinite", "inner", "intense",
    "iron", "ivory", "jade", "keen", "kind", "kinetic", "latent", "lateral", "leading", "lean",
    "light", "limpid", "linear", "lively", "lofty", "lone", "lucid", "luminous", "lunar", "lush",
    "magic", "magnetic", "majestic", "mellow", "mighty", "mild", "misty", "modern", "modest", "molten",
    "monochrome", "mystic", "narrow", "native", "natural", "neat", "nebular", "nimble", "noble", "nomadic"
]

def generate_random_string():
  adj = random.choice(ADJECTIVES)
  noun = random.choice(NOUNS)
  number = str(random.randint(10,90))
  
  r_code = adj + noun + number
  
  return r_code

def create_access_code():
  return generate_random_string().upper()
"""
Generates app/src/main/assets/questions.json for Quiz Master.

Strategy: mix curated, verifiable trivia (geography, science, history,
sports, landmarks, astronomy, Indian states) with procedurally generated
math/logic questions. The math questions guarantee we can always reach
exactly 1000 unique questions without ever repeating one, and their
difficulty is scaled by level (1-100) so the quiz gets harder as you go.

Run with:  python3 generate_questions.py
Output:    questions.json (in this folder) - copy it into
           app/src/main/assets/questions.json to use it in the app.

Feel free to edit the data lists below and re-run this to regenerate
the question bank (e.g. to add your own categories or swap topics).
"""
import json
import random

random.seed(42)

TOTAL_LEVELS = 100
QUESTIONS_PER_LEVEL = 10
TOTAL_QUESTIONS = TOTAL_LEVELS * QUESTIONS_PER_LEVEL

# ---------------------------------------------------------------------
# Curated data
# ---------------------------------------------------------------------

# (country, capital, continent, currency)
COUNTRIES = [
    ("United States", "Washington, D.C.", "North America", "US Dollar"),
    ("Canada", "Ottawa", "North America", "Canadian Dollar"),
    ("Mexico", "Mexico City", "North America", "Mexican Peso"),
    ("Brazil", "Brasilia", "South America", "Brazilian Real"),
    ("Argentina", "Buenos Aires", "South America", "Argentine Peso"),
    ("Chile", "Santiago", "South America", "Chilean Peso"),
    ("Peru", "Lima", "South America", "Peruvian Sol"),
    ("Colombia", "Bogota", "South America", "Colombian Peso"),
    ("Venezuela", "Caracas", "South America", "Venezuelan Bolivar"),
    ("United Kingdom", "London", "Europe", "British Pound"),
    ("France", "Paris", "Europe", "Euro"),
    ("Germany", "Berlin", "Europe", "Euro"),
    ("Italy", "Rome", "Europe", "Euro"),
    ("Spain", "Madrid", "Europe", "Euro"),
    ("Portugal", "Lisbon", "Europe", "Euro"),
    ("Netherlands", "Amsterdam", "Europe", "Euro"),
    ("Belgium", "Brussels", "Europe", "Euro"),
    ("Switzerland", "Bern", "Europe", "Swiss Franc"),
    ("Austria", "Vienna", "Europe", "Euro"),
    ("Sweden", "Stockholm", "Europe", "Swedish Krona"),
    ("Norway", "Oslo", "Europe", "Norwegian Krone"),
    ("Denmark", "Copenhagen", "Europe", "Danish Krone"),
    ("Finland", "Helsinki", "Europe", "Euro"),
    ("Poland", "Warsaw", "Europe", "Polish Zloty"),
    ("Greece", "Athens", "Europe", "Euro"),
    ("Ireland", "Dublin", "Europe", "Euro"),
    ("Russia", "Moscow", "Europe", "Russian Ruble"),
    ("Ukraine", "Kyiv", "Europe", "Ukrainian Hryvnia"),
    ("Czech Republic", "Prague", "Europe", "Czech Koruna"),
    ("Hungary", "Budapest", "Europe", "Hungarian Forint"),
    ("Romania", "Bucharest", "Europe", "Romanian Leu"),
    ("Turkey", "Ankara", "Asia", "Turkish Lira"),
    ("China", "Beijing", "Asia", "Chinese Yuan"),
    ("Japan", "Tokyo", "Asia", "Japanese Yen"),
    ("South Korea", "Seoul", "Asia", "South Korean Won"),
    ("India", "New Delhi", "Asia", "Indian Rupee"),
    ("Pakistan", "Islamabad", "Asia", "Pakistani Rupee"),
    ("Bangladesh", "Dhaka", "Asia", "Bangladeshi Taka"),
    ("Sri Lanka", "Sri Jayawardenepura Kotte", "Asia", "Sri Lankan Rupee"),
    ("Nepal", "Kathmandu", "Asia", "Nepalese Rupee"),
    ("Indonesia", "Jakarta", "Asia", "Indonesian Rupiah"),
    ("Thailand", "Bangkok", "Asia", "Thai Baht"),
    ("Vietnam", "Hanoi", "Asia", "Vietnamese Dong"),
    ("Philippines", "Manila", "Asia", "Philippine Peso"),
    ("Malaysia", "Kuala Lumpur", "Asia", "Malaysian Ringgit"),
    ("Singapore", "Singapore", "Asia", "Singapore Dollar"),
    ("Saudi Arabia", "Riyadh", "Asia", "Saudi Riyal"),
    ("United Arab Emirates", "Abu Dhabi", "Asia", "UAE Dirham"),
    ("Israel", "Jerusalem", "Asia", "Israeli Shekel"),
    ("Iran", "Tehran", "Asia", "Iranian Rial"),
    ("Iraq", "Baghdad", "Asia", "Iraqi Dinar"),
    ("Afghanistan", "Kabul", "Asia", "Afghan Afghani"),
    ("Kazakhstan", "Astana", "Asia", "Kazakhstani Tenge"),
    ("Egypt", "Cairo", "Africa", "Egyptian Pound"),
    ("Nigeria", "Abuja", "Africa", "Nigerian Naira"),
    ("South Africa", "Pretoria", "Africa", "South African Rand"),
    ("Kenya", "Nairobi", "Africa", "Kenyan Shilling"),
    ("Ethiopia", "Addis Ababa", "Africa", "Ethiopian Birr"),
    ("Morocco", "Rabat", "Africa", "Moroccan Dirham"),
    ("Algeria", "Algiers", "Africa", "Algerian Dinar"),
    ("Ghana", "Accra", "Africa", "Ghanaian Cedi"),
    ("Tanzania", "Dodoma", "Africa", "Tanzanian Shilling"),
    ("Uganda", "Kampala", "Africa", "Ugandan Shilling"),
    ("Zimbabwe", "Harare", "Africa", "Zimbabwean Dollar"),
    ("Australia", "Canberra", "Oceania", "Australian Dollar"),
    ("New Zealand", "Wellington", "Oceania", "New Zealand Dollar"),
    ("Fiji", "Suva", "Oceania", "Fijian Dollar"),
    ("Cuba", "Havana", "North America", "Cuban Peso"),
    ("Jamaica", "Kingston", "North America", "Jamaican Dollar"),
    ("Panama", "Panama City", "North America", "Panamanian Balboa"),
    ("Costa Rica", "San Jose", "North America", "Costa Rican Colon"),
    ("Guatemala", "Guatemala City", "North America", "Guatemalan Quetzal"),
    ("Bolivia", "Sucre", "South America", "Bolivian Boliviano"),
    ("Ecuador", "Quito", "South America", "US Dollar"),
    ("Paraguay", "Asuncion", "South America", "Paraguayan Guarani"),
    ("Uruguay", "Montevideo", "South America", "Uruguayan Peso"),
    ("Iceland", "Reykjavik", "Europe", "Icelandic Krona"),
    ("Croatia", "Zagreb", "Europe", "Euro"),
    ("Serbia", "Belgrade", "Europe", "Serbian Dinar"),
    ("Bulgaria", "Sofia", "Europe", "Bulgarian Lev"),
    ("Slovakia", "Bratislava", "Europe", "Euro"),
    ("Slovenia", "Ljubljana", "Europe", "Euro"),
    ("Lithuania", "Vilnius", "Europe", "Euro"),
    ("Latvia", "Riga", "Europe", "Euro"),
    ("Estonia", "Tallinn", "Europe", "Euro"),
    ("Belarus", "Minsk", "Europe", "Belarusian Ruble"),
    ("Mongolia", "Ulaanbaatar", "Asia", "Mongolian Tugrik"),
    ("Myanmar", "Naypyidaw", "Asia", "Myanmar Kyat"),
    ("Cambodia", "Phnom Penh", "Asia", "Cambodian Riel"),
    ("Laos", "Vientiane", "Asia", "Lao Kip"),
    ("Jordan", "Amman", "Asia", "Jordanian Dinar"),
    ("Lebanon", "Beirut", "Asia", "Lebanese Pound"),
    ("Qatar", "Doha", "Asia", "Qatari Riyal"),
    ("Kuwait", "Kuwait City", "Asia", "Kuwaiti Dinar"),
    ("Oman", "Muscat", "Asia", "Omani Rial"),
    ("Libya", "Tripoli", "Africa", "Libyan Dinar"),
    ("Tunisia", "Tunis", "Africa", "Tunisian Dinar"),
    ("Sudan", "Khartoum", "Africa", "Sudanese Pound"),
    ("Senegal", "Dakar", "Africa", "West African CFA Franc"),
    ("Zambia", "Lusaka", "Africa", "Zambian Kwacha"),
    ("Angola", "Luanda", "Africa", "Angolan Kwanza"),
    ("Mozambique", "Maputo", "Africa", "Mozambican Metical"),
    ("Madagascar", "Antananarivo", "Africa", "Malagasy Ariary"),
]

# (name, symbol, atomic_number) - first 60 elements
ELEMENTS = [
    ("Hydrogen", "H", 1), ("Helium", "He", 2), ("Lithium", "Li", 3),
    ("Beryllium", "Be", 4), ("Boron", "B", 5), ("Carbon", "C", 6),
    ("Nitrogen", "N", 7), ("Oxygen", "O", 8), ("Fluorine", "F", 9),
    ("Neon", "Ne", 10), ("Sodium", "Na", 11), ("Magnesium", "Mg", 12),
    ("Aluminium", "Al", 13), ("Silicon", "Si", 14), ("Phosphorus", "P", 15),
    ("Sulfur", "S", 16), ("Chlorine", "Cl", 17), ("Argon", "Ar", 18),
    ("Potassium", "K", 19), ("Calcium", "Ca", 20), ("Scandium", "Sc", 21),
    ("Titanium", "Ti", 22), ("Vanadium", "V", 23), ("Chromium", "Cr", 24),
    ("Manganese", "Mn", 25), ("Iron", "Fe", 26), ("Cobalt", "Co", 27),
    ("Nickel", "Ni", 28), ("Copper", "Cu", 29), ("Zinc", "Zn", 30),
    ("Gallium", "Ga", 31), ("Germanium", "Ge", 32), ("Arsenic", "As", 33),
    ("Selenium", "Se", 34), ("Bromine", "Br", 35), ("Krypton", "Kr", 36),
    ("Rubidium", "Rb", 37), ("Strontium", "Sr", 38), ("Yttrium", "Y", 39),
    ("Zirconium", "Zr", 40), ("Niobium", "Nb", 41), ("Molybdenum", "Mo", 42),
    ("Technetium", "Tc", 43), ("Ruthenium", "Ru", 44), ("Rhodium", "Rh", 45),
    ("Palladium", "Pd", 46), ("Silver", "Ag", 47), ("Cadmium", "Cd", 48),
    ("Indium", "In", 49), ("Tin", "Sn", 50), ("Antimony", "Sb", 51),
    ("Tellurium", "Te", 52), ("Iodine", "I", 53), ("Xenon", "Xe", 54),
    ("Cesium", "Cs", 55), ("Barium", "Ba", 56), ("Lanthanum", "La", 57),
    ("Cerium", "Ce", 58), ("Praseodymium", "Pr", 59), ("Neodymium", "Nd", 60),
]

# (state, capital) - Indian states
INDIAN_STATES = [
    ("Andhra Pradesh", "Amaravati"), ("Arunachal Pradesh", "Itanagar"),
    ("Assam", "Dispur"), ("Bihar", "Patna"), ("Chhattisgarh", "Raipur"),
    ("Goa", "Panaji"), ("Gujarat", "Gandhinagar"), ("Haryana", "Chandigarh"),
    ("Himachal Pradesh", "Shimla"), ("Jharkhand", "Ranchi"),
    ("Karnataka", "Bengaluru"), ("Kerala", "Thiruvananthapuram"),
    ("Madhya Pradesh", "Bhopal"), ("Maharashtra", "Mumbai"),
    ("Manipur", "Imphal"), ("Meghalaya", "Shillong"), ("Mizoram", "Aizawl"),
    ("Nagaland", "Kohima"), ("Odisha", "Bhubaneswar"), ("Punjab", "Chandigarh"),
    ("Rajasthan", "Jaipur"), ("Sikkim", "Gangtok"), ("Tamil Nadu", "Chennai"),
    ("Telangana", "Hyderabad"), ("Tripura", "Agartala"),
    ("Uttar Pradesh", "Lucknow"), ("Uttarakhand", "Dehradun"),
    ("West Bengal", "Kolkata"),
]

# (landmark, country)
LANDMARKS = [
    ("The Eiffel Tower", "France"), ("The Great Wall", "China"),
    ("The Colosseum", "Italy"), ("The Statue of Liberty", "United States"),
    ("Machu Picchu", "Peru"), ("The Taj Mahal", "India"),
    ("The Pyramids of Giza", "Egypt"), ("Big Ben", "United Kingdom"),
    ("The Leaning Tower of Pisa", "Italy"), ("Christ the Redeemer", "Brazil"),
    ("The Sydney Opera House", "Australia"), ("Stonehenge", "United Kingdom"),
    ("The Acropolis", "Greece"), ("Mount Fuji", "Japan"),
    ("The Sagrada Familia", "Spain"), ("Petra", "Jordan"),
    ("The Burj Khalifa", "United Arab Emirates"), ("Angkor Wat", "Cambodia"),
    ("Niagara Falls", "Canada"), ("The Kremlin", "Russia"),
    ("The Brandenburg Gate", "Germany"), ("Mount Kilimanjaro", "Tanzania"),
    ("The Forbidden City", "China"), ("Table Mountain", "South Africa"),
    ("The Alhambra", "Spain"), ("Neuschwanstein Castle", "Germany"),
    ("The Blue Mosque", "Turkey"), ("Easter Island Statues (Moai)", "Chile"),
    ("The Golden Gate Bridge", "United States"), ("Mont Saint-Michel", "France"),
    ("Chichen Itza", "Mexico"), ("The Atomium", "Belgium"),
    ("Edinburgh Castle", "United Kingdom"), ("The Little Mermaid statue", "Denmark"),
    ("Gateway of India", "India"), ("Red Square", "Russia"),
    ("The Shard", "United Kingdom"), ("CN Tower", "Canada"),
    ("The Hermitage Museum", "Russia"), ("Hagia Sophia", "Turkey"),
]

PLANET_QUESTIONS = [
    ("Which planet is closest to the Sun?", ["Mercury", "Venus", "Earth", "Mars"], 0),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1),
    ("Which is the largest planet in our solar system?", ["Saturn", "Earth", "Jupiter", "Neptune"], 2),
    ("Which planet is famous for its prominent ring system?", ["Saturn", "Mars", "Mercury", "Earth"], 0),
    ("Which planet is the hottest in the solar system?", ["Mercury", "Venus", "Mars", "Jupiter"], 1),
    ("How many planets are there in our solar system?", ["7", "8", "9", "10"], 1),
    ("Which planet is tilted on its side, causing extreme seasons?", ["Neptune", "Saturn", "Uranus", "Mars"], 2),
    ("Which planet is the farthest from the Sun?", ["Uranus", "Saturn", "Jupiter", "Neptune"], 3),
    ("Which is the smallest planet in the solar system?", ["Mars", "Mercury", "Venus", "Pluto"], 1),
    ("Which planet has a day longer than its year?", ["Mars", "Mercury", "Venus", "Earth"], 2),
    ("Which planet is often called Earth's 'twin' due to its similar size?", ["Mars", "Venus", "Mercury", "Neptune"], 1),
    ("Which star is at the center of our solar system?", ["Proxima Centauri", "The Sun", "Sirius", "Polaris"], 1),
    ("Which planet is known for the Great Red Spot, a giant storm?", ["Jupiter", "Saturn", "Mars", "Uranus"], 0),
    ("What is Earth's only natural satellite called?", ["Titan", "Europa", "The Moon", "Phobos"], 2),
    ("Which planet is the third planet from the Sun?", ["Venus", "Earth", "Mars", "Mercury"], 1),
]

SCIENCE_QUESTIONS = [
    ("What gas do plants absorb from the air for photosynthesis?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], 2),
    ("What is the chemical formula for water?", ["CO2", "H2O", "O2", "NaCl"], 1),
    ("How many bones are in the adult human body?", ["186", "206", "226", "246"], 1),
    ("What is the powerhouse of the cell?", ["Nucleus", "Ribosome", "Mitochondria", "Golgi body"], 2),
    ("Which blood type is known as the universal donor?", ["A", "B", "AB", "O negative"], 3),
    ("What force pulls objects toward the center of the Earth?", ["Magnetism", "Friction", "Gravity", "Tension"], 2),
    ("What is the boiling point of water at sea level in Celsius?", ["90", "100", "110", "120"], 1),
    ("Which organ pumps blood throughout the human body?", ["Liver", "Heart", "Lungs", "Kidney"], 1),
    ("What is the chemical symbol for gold?", ["Go", "Gd", "Au", "Ag"], 2),
    ("Which gas makes up most of Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], 1),
    ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Quartz"], 2),
    ("How many chambers does the human heart have?", ["2", "3", "4", "5"], 2),
    ("What part of the plant conducts photosynthesis?", ["Root", "Stem", "Leaf", "Flower"], 2),
    ("What is the freezing point of water in Celsius?", ["-10", "0", "10", "32"], 1),
    ("Which planet do humans currently live on?", ["Mars", "Venus", "Earth", "Mercury"], 2),
    ("What do you call an animal that eats only plants?", ["Carnivore", "Herbivore", "Omnivore", "Predator"], 1),
    ("Which sense organ is responsible for vision?", ["Ear", "Nose", "Eye", "Tongue"], 2),
    ("What is the basic unit of life?", ["Atom", "Molecule", "Cell", "Tissue"], 2),
    ("Which vitamin is produced when skin is exposed to sunlight?", ["Vitamin A", "Vitamin C", "Vitamin D", "Vitamin K"], 2),
    ("What is the process by which plants lose water through leaves called?", ["Respiration", "Transpiration", "Photosynthesis", "Germination"], 1),
    ("What type of energy is stored in food?", ["Kinetic", "Chemical", "Thermal", "Nuclear"], 1),
    ("Which metal is liquid at room temperature?", ["Iron", "Mercury", "Lead", "Tin"], 1),
    ("What is the study of living organisms called?", ["Geology", "Biology", "Chemistry", "Physics"], 1),
    ("How many pairs of chromosomes do humans have?", ["21", "22", "23", "24"], 2),
    ("What is the main gas responsible for the greenhouse effect?", ["Oxygen", "Carbon dioxide", "Helium", "Nitrogen"], 1),
    ("What organ filters waste from human blood?", ["Liver", "Kidney", "Stomach", "Lungs"], 1),
    ("Which simple machine is a ramp an example of?", ["Lever", "Pulley", "Inclined plane", "Wheel and axle"], 2),
    ("What do bees collect from flowers to make honey?", ["Pollen", "Nectar", "Water", "Sap"], 1),
    ("What is the closest star to Earth?", ["Polaris", "The Sun", "Alpha Centauri", "Sirius"], 1),
    ("What instrument is used to measure temperature?", ["Barometer", "Thermometer", "Hygrometer", "Anemometer"], 1),
    ("What is the chemical symbol for sodium?", ["So", "S", "Na", "Sd"], 2),
    ("Which part of the brain controls balance?", ["Cerebrum", "Cerebellum", "Medulla", "Thalamus"], 1),
    ("What natural phenomenon is measured using the Richter scale?", ["Hurricanes", "Earthquakes", "Tornadoes", "Floods"], 1),
    ("What is the main function of red blood cells?", ["Fight infection", "Clot blood", "Carry oxygen", "Digest food"], 2),
    ("What do you call water in its solid state?", ["Vapor", "Liquid", "Ice", "Steam"], 2),
    ("Which gas do humans exhale when they breathe out?", ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], 1),
    ("What is the largest organ in the human body?", ["Liver", "Brain", "Skin", "Heart"], 2),
    ("What causes the tides in the ocean?", ["Wind", "The Moon's gravity", "Earthquakes", "Ocean currents"], 1),
    ("What is the process of a caterpillar becoming a butterfly called?", ["Fertilization", "Metamorphosis", "Pollination", "Germination"], 1),
    ("What part of a plant absorbs water from the soil?", ["Leaf", "Stem", "Root", "Flower"], 2),
    ("Which scientist proposed the theory of gravity after seeing a falling apple?", ["Einstein", "Newton", "Galileo", "Darwin"], 1),
    ("What is the chemical symbol for iron?", ["Ir", "In", "Fe", "I"], 2),
    ("How many legs does a spider have?", ["6", "8", "10", "12"], 1),
    ("What is the speed of light approximately?", ["300 km/s", "300,000 km/s", "30,000 km/s", "3,000 km/s"], 1),
    ("What do plants release into the air that humans breathe?", ["Carbon dioxide", "Nitrogen", "Oxygen", "Methane"], 2),
    ("What is the smallest unit of an element?", ["Molecule", "Atom", "Cell", "Proton"], 1),
    ("Which sense is associated with the tongue?", ["Smell", "Touch", "Taste", "Hearing"], 2),
    ("What is the term for animals that are active at night?", ["Diurnal", "Nocturnal", "Crepuscular", "Hibernating"], 1),
    ("What state of matter has no fixed shape or volume?", ["Solid", "Liquid", "Gas", "Plasma"], 2),
    ("What do you call the path an object takes around another due to gravity?", ["Rotation", "Revolution", "Orbit", "Trajectory"], 2),
]

HISTORY_QUESTIONS = [
    ("In which year did World War II end?", ["1943", "1945", "1947", "1950"], 1),
    ("In which year did World War I begin?", ["1912", "1914", "1916", "1918"], 1),
    ("Who was the first President of the United States?", ["Thomas Jefferson", "George Washington", "John Adams", "Abraham Lincoln"], 1),
    ("In which year did India gain independence?", ["1945", "1947", "1950", "1952"], 1),
    ("Which ancient civilization built the pyramids of Giza?", ["Romans", "Greeks", "Egyptians", "Persians"], 2),
    ("Who is known as the Father of the Nation in India?", ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "Subhas Chandra Bose"], 1),
    ("In which year did the Titanic sink?", ["1905", "1912", "1920", "1931"], 1),
    ("Which empire was ruled by Julius Caesar?", ["Greek Empire", "Roman Empire", "Persian Empire", "Ottoman Empire"], 1),
    ("The Berlin Wall fell in which year?", ["1985", "1989", "1991", "1995"], 1),
    ("Who wrote the Declaration of Independence?", ["Benjamin Franklin", "Thomas Jefferson", "George Washington", "Alexander Hamilton"], 1),
    ("Which war was fought between the North and South regions of the United States?", ["Revolutionary War", "Civil War", "Mexican-American War", "War of 1812"], 1),
    ("In which century did the Renaissance begin?", ["12th century", "14th century", "16th century", "18th century"], 1),
    ("Who was the first man to walk on the Moon?", ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"], 1),
    ("Which country gifted the Statue of Liberty to the United States?", ["United Kingdom", "Spain", "France", "Italy"], 2),
    ("In which year did the French Revolution begin?", ["1769", "1789", "1799", "1804"], 1),
    ("Who was the British Prime Minister during most of World War II?", ["Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Tony Blair"], 1),
    ("Which ship did Christopher Columbus sail on his first voyage in 1492?", ["The Mayflower", "The Santa Maria", "The Beagle", "The Endeavour"], 1),
    ("The Great Wall was built primarily to protect which country?", ["Japan", "China", "Mongolia", "Korea"], 1),
    ("Who was the first Prime Minister of independent India?", ["Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Patel", "Rajendra Prasad"], 1),
    ("In which year did the Soviet Union dissolve?", ["1985", "1989", "1991", "1993"], 2),
    ("Which empire was known for building the Colosseum?", ["Greek", "Roman", "Egyptian", "Ottoman"], 1),
    ("Who painted the Mona Lisa?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], 1),
    ("Which country was first to send a human into space?", ["United States", "Soviet Union", "China", "Germany"], 1),
    ("In which year did the United States declare independence?", ["1774", "1776", "1781", "1787"], 1),
    ("Who was the Egyptian queen famous for her relationship with Mark Antony?", ["Nefertiti", "Cleopatra", "Hatshepsut", "Ankhesenamun"], 1),
    ("Which event started World War I?", ["Sinking of the Lusitania", "Assassination of Archduke Franz Ferdinand", "Invasion of Poland", "Treaty of Versailles"], 1),
    ("Who is considered the founder of the Mughal Empire in India?", ["Akbar", "Babur", "Aurangzeb", "Shah Jahan"], 1),
    ("Which document, signed in 1215, limited the power of the English king?", ["Magna Carta", "Bill of Rights", "Treaty of Paris", "Declaration of Independence"], 0),
    ("Who was the leader of Nazi Germany during World War II?", ["Joseph Stalin", "Adolf Hitler", "Benito Mussolini", "Francisco Franco"], 1),
    ("The ancient Olympic Games originated in which country?", ["Italy", "Greece", "Egypt", "Turkey"], 1),
    ("Who built the Taj Mahal?", ["Akbar", "Shah Jahan", "Aurangzeb", "Humayun"], 1),
    ("Which war ended with the Treaty of Versailles in 1919?", ["World War II", "World War I", "The Cold War", "The Crimean War"], 1),
    ("Who was the first emperor of China to unify the country?", ["Qin Shi Huang", "Sun Tzu", "Confucius", "Mao Zedong"], 0),
    ("In which year did Apollo 11 land on the Moon?", ["1965", "1969", "1972", "1975"], 1),
    ("Which civilization is credited with inventing the wheel?", ["Egyptians", "Mesopotamians", "Romans", "Greeks"], 1),
    ("Who was the famous queen of England during the defeat of the Spanish Armada?", ["Queen Victoria", "Elizabeth I", "Mary I", "Anne"], 1),
    ("Which country was divided by the Berlin Wall during the Cold War?", ["France", "Germany", "Poland", "Austria"], 1),
    ("Who led the Salt March in India in 1930?", ["Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Bhagat Singh"], 1),
    ("Which empire was ruled from Constantinople for centuries?", ["Roman Empire", "Byzantine Empire", "Persian Empire", "Ottoman Empire"], 1),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", ["Amelia Earhart", "Bessie Coleman", "Harriet Quimby", "Jacqueline Cochran"], 0),
    ("Which country was formerly known as Persia?", ["Iraq", "Iran", "Turkey", "Syria"], 1),
    ("Who was the Roman general famously defeated at the Battle of Actium?", ["Julius Caesar", "Mark Antony", "Pompey", "Augustus"], 1),
    ("In which year did the Wright brothers achieve the first powered flight?", ["1899", "1903", "1908", "1912"], 1),
    ("Which country built the first railway network in the 1800s?", ["United States", "United Kingdom", "Germany", "France"], 1),
    ("Who was the Indian freedom fighter known for the phrase 'Give me blood, and I shall give you freedom'?", ["Bhagat Singh", "Subhas Chandra Bose", "Chandrashekhar Azad", "Lala Lajpat Rai"], 1),
    ("Which ancient wonder was located in the city of Alexandria?", ["Hanging Gardens", "Lighthouse of Alexandria", "Colossus of Rhodes", "Temple of Artemis"], 1),
    ("Who succeeded Mahatma Gandhi's vision and became India's first Deputy Prime Minister?", ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Rajendra Prasad", "Maulana Azad"], 1),
    ("Which war is commonly referred to as 'The Great War'?", ["World War II", "World War I", "The Cold War", "The Korean War"], 1),
    ("In which century did Christopher Columbus reach the Americas?", ["13th century", "15th century", "17th century", "19th century"], 1),
    ("Who was the longest-reigning British monarch before Queen Elizabeth II's record?", ["Queen Victoria", "King George III", "King Henry VIII", "Queen Anne"], 0),
]

SPORTS_QUESTIONS = [
    ("How many players are on a cricket team on the field at one time?", ["9", "10", "11", "12"], 2),
    ("How many players are on a football (soccer) team on the field at one time?", ["9", "10", "11", "12"], 2),
    ("How many rings are on the Olympic flag?", ["4", "5", "6", "7"], 1),
    ("In tennis, what is a score of zero called?", ["Love", "Nil", "Ace", "Deuce"], 0),
    ("How many players are on a basketball team on the court at one time?", ["4", "5", "6", "7"], 1),
    ("In which sport would you perform a slam dunk?", ["Volleyball", "Basketball", "Badminton", "Tennis"], 1),
    ("How often are the Summer Olympic Games held?", ["Every 2 years", "Every 4 years", "Every 5 years", "Every 6 years"], 1),
    ("What is the maximum score possible with three darts in one turn (using a single triple-20 trio)?", ["120", "150", "160", "180"], 3),
    ("In golf, what is one stroke under par called?", ["Bogey", "Birdie", "Eagle", "Albatross"], 1),
    ("How many holes are played in a standard round of golf?", ["9", "16", "18", "20"], 2),
    ("Which sport uses terms like 'love', 'deuce', and 'ace'?", ["Badminton", "Tennis", "Table Tennis", "Squash"], 1),
    ("How many players make up a standard volleyball team on the court?", ["5", "6", "7", "8"], 1),
    ("In boxing, how many rounds are typically in a professional championship bout?", ["8", "10", "12", "15"], 2),
    ("Which country is credited with inventing the sport of cricket?", ["Australia", "England", "India", "South Africa"], 1),
    ("What is the term for scoring three goals in a single soccer match by one player?", ["Double", "Hat-trick", "Triple play", "Treble"], 1),
    ("How long is a marathon race in kilometers (approximately)?", ["32 km", "38 km", "42 km", "50 km"], 2),
    ("In chess, how many squares are on the board?", ["32", "48", "64", "100"], 2),
    ("Which sport is played at Wimbledon?", ["Tennis", "Golf", "Cricket", "Rugby"], 0),
    ("How many players are on a rugby union team on the field?", ["11", "13", "15", "17"], 2),
    ("What shape is a baseball field's infield?", ["Circle", "Square (diamond)", "Triangle", "Rectangle"], 1),
    ("In swimming, what stroke involves swimming on your back?", ["Freestyle", "Backstroke", "Breaststroke", "Butterfly"], 1),
    ("How many players are on each side in a standard game of badminton doubles?", ["1", "2", "3", "4"], 1),
    ("Which trophy is awarded to the winner of the FIFA World Cup?", ["The Ashes", "The FIFA World Cup Trophy", "The Stanley Cup", "The Davis Cup"], 1),
    ("In American football, how many points is a touchdown worth?", ["3", "5", "6", "7"], 2),
    ("Which sport features the term 'wicket'?", ["Baseball", "Cricket", "Hockey", "Lacrosse"], 1),
    ("How many players are on an ice hockey team on the ice at once (excluding goalie)?", ["4", "5", "6", "7"], 1),
    ("What is the national sport of Japan?", ["Judo", "Sumo wrestling", "Karate", "Baseball"], 1),
    ("Which Grand Slam tennis tournament is played on clay courts?", ["Wimbledon", "US Open", "French Open", "Australian Open"], 2),
    ("How many players are on a polo team?", ["3", "4", "5", "6"], 1),
    ("In which sport do players use a shuttlecock?", ["Tennis", "Squash", "Badminton", "Table Tennis"], 2),
    ("What is the diameter of a basketball hoop in inches (approximately)?", ["12 inches", "18 inches", "24 inches", "30 inches"], 1),
    ("Which country has won the most FIFA World Cups (as of recent history)?", ["Germany", "Argentina", "Brazil", "Italy"], 2),
    ("What is the term for a perfect score of 300 in ten-pin bowling?", ["A turkey", "A perfect game", "A strike-out", "A clean sweep"], 1),
    ("How many periods are in a standard ice hockey game?", ["2", "3", "4", "5"], 1),
    ("In athletics, what is the name of the long-distance race of 42.195 km?", ["Sprint", "Marathon", "Relay", "Steeplechase"], 1),
    ("Which sport is associated with the term 'love game'?", ["Tennis", "Cricket", "Golf", "Rugby"], 0),
    ("How many players are on a standard netball team on court?", ["5", "6", "7", "8"], 2),
    ("Which event in athletics involves jumping over a bar using a flexible pole?", ["High jump", "Long jump", "Pole vault", "Triple jump"], 2),
    ("What is the maximum number of clubs a golfer can carry in a bag during a round?", ["12", "14", "16", "18"], 1),
    ("In which sport is the term 'checkmate' used?", ["Carrom", "Chess", "Checkers", "Backgammon"], 1),
]

# ---------------------------------------------------------------------
# Build the trivia pool
# ---------------------------------------------------------------------

def make_mc(question, options, correct_index, category):
    return {
        "category": category,
        "question": question,
        "options": options,
        "correctIndex": correct_index,
    }


def with_distractors(correct, all_values, count=3):
    pool = [v for v in all_values if v != correct]
    chosen = random.sample(pool, min(count, len(pool)))
    options = chosen + [correct]
    random.shuffle(options)
    return options, options.index(correct)


trivia_pool = []

all_capitals = [c[1] for c in COUNTRIES]
all_continents = sorted(set(c[2] for c in COUNTRIES))
all_currencies = sorted(set(c[3] for c in COUNTRIES))

for name, capital, continent, currency in COUNTRIES:
    opts, idx = with_distractors(capital, all_capitals)
    trivia_pool.append(make_mc(f"What is the capital of {name}?", opts, idx, "Geography"))

    opts, idx = with_distractors(continent, all_continents)
    trivia_pool.append(make_mc(f"Which continent is {name} located in?", opts, idx, "Geography"))

    opts, idx = with_distractors(currency, all_currencies)
    trivia_pool.append(make_mc(f"What is the official/primary currency of {name}?", opts, idx, "Geography"))

all_symbols = [e[1] for e in ELEMENTS]
for ename, symbol, number in ELEMENTS:
    opts, idx = with_distractors(symbol, all_symbols)
    trivia_pool.append(make_mc(f"What is the chemical symbol for {ename}?", opts, idx, "Science"))

    wrong_numbers = set()
    while len(wrong_numbers) < 3:
        delta = random.randint(1, 10) * random.choice([-1, 1])
        candidate = number + delta
        if candidate > 0 and candidate != number:
            wrong_numbers.add(candidate)
    opts = [str(number)] + [str(n) for n in wrong_numbers]
    random.shuffle(opts)
    trivia_pool.append(make_mc(f"What is the atomic number of {ename}?", opts, opts.index(str(number)), "Science"))

all_state_capitals = [s[1] for s in INDIAN_STATES]
for state, capital in INDIAN_STATES:
    opts, idx = with_distractors(capital, all_state_capitals)
    trivia_pool.append(make_mc(f"What is the capital of the Indian state {state}?", opts, idx, "Indian GK"))

all_landmark_countries = sorted(set(c for _, c in LANDMARKS))
for landmark, country in LANDMARKS:
    opts, idx = with_distractors(country, all_landmark_countries)
    trivia_pool.append(make_mc(f"{landmark} is located in which country?", opts, idx, "Landmarks"))

for q, opts, idx in PLANET_QUESTIONS:
    trivia_pool.append(make_mc(q, opts, idx, "Astronomy"))

for q, opts, idx in SCIENCE_QUESTIONS:
    trivia_pool.append(make_mc(q, opts, idx, "Science"))

for q, opts, idx in HISTORY_QUESTIONS:
    trivia_pool.append(make_mc(q, opts, idx, "History"))

for q, opts, idx in SPORTS_QUESTIONS:
    trivia_pool.append(make_mc(q, opts, idx, "Sports"))

random.shuffle(trivia_pool)

print(f"Curated trivia pool: {len(trivia_pool)} questions")

# ---------------------------------------------------------------------
# Math/logic generator (fills remaining slots, difficulty scales by level)
# ---------------------------------------------------------------------

seen_math_questions = set()


def distractors_numeric(correct):
    options = {correct}
    while len(options) < 4:
        delta = random.choice([-1, 1]) * random.randint(1, max(3, abs(correct) // 5 + 2))
        candidate = correct + delta
        if candidate != correct:
            options.add(candidate)
    opts = list(options)
    random.shuffle(opts)
    return [str(o) for o in opts], opts.index(correct)


def gen_math_question(level):
    for _ in range(50):  # retry on rare duplicate
        if level <= 25:
            a, b = random.randint(1, 50), random.randint(1, 50)
            op = random.choice(["+", "-"])
            if op == "-" and b > a:
                a, b = b, a
            answer = a + b if op == "+" else a - b
            text = f"What is {a} {op} {b}?"
        elif level <= 50:
            a, b = random.randint(2, 20), random.randint(2, 12)
            op = random.choice(["*", "+", "-"])
            if op == "*":
                answer = a * b
                text = f"What is {a} x {b}?"
            else:
                a2, b2 = random.randint(20, 200), random.randint(20, 200)
                if op == "-" and b2 > a2:
                    a2, b2 = b2, a2
                answer = a2 + b2 if op == "+" else a2 - b2
                text = f"What is {a2} {op} {b2}?"
        elif level <= 75:
            kind = random.choice(["mul2", "square", "percent"])
            if kind == "mul2":
                a, b = random.randint(11, 40), random.randint(11, 30)
                answer = a * b
                text = f"What is {a} x {b}?"
            elif kind == "square":
                a = random.randint(4, 25)
                answer = a * a
                text = f"What is {a} squared ({a}\u00b2)?"
            else:
                pct = random.choice([10, 20, 25, 50, 75])
                base = random.randint(2, 40) * 4
                answer = base * pct // 100
                text = f"What is {pct}% of {base}?"
        else:
            kind = random.choice(["multistep", "algebra", "sqrt"])
            if kind == "multistep":
                a, b, c = random.randint(2, 12), random.randint(2, 12), random.randint(1, 50)
                answer = a * b + c
                text = f"What is ({a} x {b}) + {c}?"
            elif kind == "algebra":
                x = random.randint(2, 50)
                add = random.randint(1, 50)
                total = x + add
                answer = x
                text = f"Solve for x: x + {add} = {total}"
            else:
                bases = [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]
                sq = random.choice(bases)
                answer = int(sq ** 0.5)
                text = f"What is the square root of {sq}?"

        if text not in seen_math_questions:
            seen_math_questions.add(text)
            options, idx = distractors_numeric(answer)
            return make_mc(text, options, idx, "Math")
    raise RuntimeError("Could not generate a unique math question - widen the ranges")


# ---------------------------------------------------------------------
# Assemble levels
# ---------------------------------------------------------------------

trivia_counts = [7] * 43 + [6] * 57  # sums to 643; adjusted below if pool differs
total_trivia_needed = sum(min(c, QUESTIONS_PER_LEVEL) for c in trivia_counts)

# If our curated pool doesn't have exactly 643, scale gracefully:
pool_size = len(trivia_pool)
if pool_size < total_trivia_needed:
    # Reduce trivia per level evenly until it fits
    scale = pool_size / total_trivia_needed
    trivia_counts = [max(0, int(c * scale)) for c in trivia_counts]

pool_iter = iter(trivia_pool)
all_questions = []

difficulty_for_level = lambda lvl: (
    "easy" if lvl <= 25 else "medium" if lvl <= 50 else "hard" if lvl <= 75 else "expert"
)

for level in range(1, TOTAL_LEVELS + 1):
    needed_trivia = trivia_counts[level - 1]
    level_questions = []

    for _ in range(needed_trivia):
        try:
            level_questions.append(next(pool_iter))
        except StopIteration:
            break

    while len(level_questions) < QUESTIONS_PER_LEVEL:
        level_questions.append(gen_math_question(level))

    random.shuffle(level_questions)

    for i, q in enumerate(level_questions, start=1):
        all_questions.append({
            "id": f"L{level}Q{i}",
            "level": level,
            "category": q["category"],
            "question": q["question"],
            "options": q["options"],
            "correctIndex": q["correctIndex"],
            "difficulty": difficulty_for_level(level),
        })

# ---------------------------------------------------------------------
# Validate
# ---------------------------------------------------------------------

assert len(all_questions) == TOTAL_QUESTIONS, f"Expected {TOTAL_QUESTIONS}, got {len(all_questions)}"

by_level = {}
for q in all_questions:
    by_level.setdefault(q["level"], []).append(q)
for lvl in range(1, TOTAL_LEVELS + 1):
    assert len(by_level.get(lvl, [])) == QUESTIONS_PER_LEVEL, f"Level {lvl} has wrong count"

texts = [q["question"] for q in all_questions]
assert len(texts) == len(set(texts)), "Duplicate question text found!"

for q in all_questions:
    assert len(q["options"]) == 4
    assert 0 <= q["correctIndex"] <= 3

print(f"Generated {len(all_questions)} unique questions across {TOTAL_LEVELS} levels. Validation passed.")

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print("Wrote questions.json")

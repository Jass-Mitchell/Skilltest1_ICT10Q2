
        def main():
            elements = {
                "H": ["Hydrogen", 1, 1.008],
                "C": ["Carbon", 6, 12.011],
                "N": ["Nitrogen", 7, 14.007],
                "O": ["Oxygen", 8, 15.999],
                "P": ["Phosphorus", 15, 30.974],
                "S": ["Sulfur", 16, 32.06],
                "F": ["Fluorine", 9, 18.998],
                "Cl": ["Chlorine", 17, 35.45]
            }

            symbol = Element("symbol").value.strip().capitalize()

            element = elements.get(symbol, ["Element not found!", "", ""])

            print("Element Symbol:", symbol)
            print("Element Name:", element[0])
            print("Atomic Number:", element[1])
            print("Atomic Mass:", element[2])
 

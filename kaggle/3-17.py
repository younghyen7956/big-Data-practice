import pandas as pd
from scipy.stats import wilcoxon

data = {
    "weight": [630, 610, 625, 615, 622, 618, 623, 619, 620, 624, 616, 621, 617, 629, 626, 620, 618, 622, 625, 615,
               628, 617, 624, 619, 621, 623, 620, 622, 618, 625, 616, 629, 620, 624, 617, 621, 623, 619, 625, 618,
               622, 620, 624, 617, 621, 623, 619, 625, 618, 622]
}

df = pd.DataFrame(data)

print(wilcoxon(df['weight']-620,alternative="greater"))



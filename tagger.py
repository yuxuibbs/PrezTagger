import pandas as pd
import numpy as np

# regexes for cleaning the file that has all the prez questions: 
#   \n\([246] pts.\)\s+
#   \n\(Answer: (#.+ .*)\)

data = pd.read_csv('questions.txt', sep='~', header=None)
data.columns = ['range', '6 pts', '4 pts', '2 pts', 'answer']
# make new column for numerical answer
data['numerical answer'] = data['answer'].str.extract('(\d+)', expand=False).astype(int)
# make new column to correct the range to either 1-12 or 13-24
# all the answers in the numerical answer column are 1-24
data['corrected range'] = np.where(((data['numerical answer'] <= 12)), "1-12", "13-24")
# list of topics/themes
themes = ['Cabinet Members', 'Domestic Affairs', 'Election Opponents', 
          'First Ladies', 'Foreign Affairs', 'Occupations and Posts', 
          'Presidential Firsts', 'Presidential Quotes', 'Scandals', 
          'Slogans', 'Vice Presidents']

# list of cabinet positions
cabinet_postions = ['department of state', 'department of the treasury', 
                    'department of interior', 'department of agriculture', 
                    'department of justice', 'department of labor', 
                    'department of commerce', 'department of defense', 
                    'department of housing and urban development', 
                    'department of transportation', 'department of energy', 
                    'department of education', 
                    'department of health and human services', 
                    'department of veteran affairs', 
                    'department of homeland security']

# list of first ladies
# list taken from https://www.britannica.com/topic/list-of-first-ladies-of-the-United-States-1788870
first_ladies = ['Abigail Adams', 'Louisa Adams', 'Ellen Arthur', 
                'Barbara Bush', 'Laura Bush', 'Rosalynn Carter', 
                'Frances Cleveland', 'Hillary Rodham Clinton', 
                'Grace Coolidge', 'Mamie Eisenhower', 'Abigail Fillmore', 
                'Betty Ford', 'Lucretia Garfield', 'Julia Grant', 
                'Florence Harding', 'Anna Harrison', 'Caroline Harrison', 
                'Lucy Hayes', 'Lou Hoover', 'Rachel Jackson', 
                'Martha Jefferson', 'Eliza Johnson', 'Lady Bird Johnson', 
                'Jacqueline Kennedy', 'Jacqueline Kennedy Onassis', 
                'Mary Todd Lincoln', 'Dolley Madison', 'Ida McKinley', 
                'Elizabeth Monroe', 'Pat Nixon', 'Michelle Obama', 
                'Jane Pierce', 'Sarah Polk', 'Nancy Reagan', 
                'Edith Roosevelt', 'Eleanor Roosevelt', 'Helen Taft', 
                'Margaret Taylor', 'Bess Truman', 'Melania Trump', 
                'Julia Tyler', 'Letitia Tyler', 'Hannah Van Buren', 
                'Martha Washington', 'Edith Wilson', 'Ellen Wilson']





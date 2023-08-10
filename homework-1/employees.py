sql_empl = "INSERT INTO employees (employee_id, first_name, last_name , title, birth_date , notes) VALUES (%s, %s, %s, %s, %s, %s)"
val_empl = [
    (1, "Nancy", "Davolio", "Sales Representative", "1948-12-08", "Education includes a BA in psychology from Colorado "
                                                                  "State University in 1970.  She also completed The "
                                                                  "Art of the Cold Call.  Nancy is a member of "
                                                                  "Toastmasters International."
     ),
    (2, "Andrew", "Fuller", "Vice President, Sales", "1952-02-19", "Andrew received his BTS commercial in 1974 and a "
                                                                   "Ph.D. in international marketing from the "
                                                                   "University of Dallas in 1981.  He is fluent in "
                                                                   "French and Italian and reads German.  He joined "
                                                                   "the company as a sales representative, "
                                                                   "was promoted to sales manager in January 1992 and "
                                                                   "to vice president of sales in March 1993.  Andrew "
                                                                   "is a member of the Sales Management Roundtable, "
                                                                   "the Seattle Chamber of Commerce, and the Pacific "
                                                                   "Rim Importers Association."
     ),
    (3, "Janet", "Leverling", "Sales Representative", "1963-08-30", "Janet has a BS degree in chemistry from Boston "
                                                                    "College (1984).  She has also completed a "
                                                                    "certificate program in food retailing "
                                                                    "management.  Janet was hired as a sales "
                                                                    "associate in 1991 and promoted to sales "
                                                                    "representative in February 1992."
     ),
    (4, "Margaret", "Peacock", "Sales Representative", "1937-09-19", "Margaret holds a BA in English literature from "
                                                                     "Concordia College (1958) and an MA from the "
                                                                     "American Institute of Culinary Arts (1966).  "
                                                                     "She was assigned to the London office "
                                                                     "temporarily from July through November 1992."
     ),
    (5, "Steven", "Buchanan", "Sales Manager", "1955-03-04", "Steven Buchanan graduated from St. Andrews University, "
                                                             "Scotland, with a BSC degree in 1976.  Upon joining the "
                                                             "company as a sales representative in 1992, he spent 6 "
                                                             "months in an orientation program at the Seattle office "
                                                             "and then returned to his permanent post in London.  He "
                                                             "was promoted to sales manager in March 1993.  Mr. "
                                                             "Buchanan has completed the courses Successful "
                                                             "Telemarketing and International Sales Management.  He "
                                                             "is fluent in French."
     ),
    (6, "Michael", "Suyama", "Sales Representative", "1963-07-02", "Michael is a graduate of Sussex University (MA, "
                                                                   "economics, 1983) and the University of California "
                                                                   "at Los Angeles (MBA, marketing, 1986).  He has "
                                                                   "also taken the courses Multi-Cultural Selling and "
                                                                   "Time Management for the Sales Professional.  He "
                                                                   "is fluent in Japanese and can read and write "
                                                                   "French, Portuguese, and Spanish."
     ),
    (7, "Robert", "King", "Sales Representative", "1960-05-29", "Robert King served in the Peace Corps and traveled "
                                                                "extensively before completing his degree in English "
                                                                "at the University of Michigan in 1992, the year he "
                                                                "joined the company.  After completing a course "
                                                                "entitled Selling in Europe, he was transferred to "
                                                                "the London office in March 1993."
     ),
    (8, "Laura", "Callahan", "Inside Sales Coordinator", "1958-01-09", "Laura received a BA in psychology from the "
                                                                       "University of Washington.  She has also "
                                                                       "completed a course in business French.  She "
                                                                       "reads and writes French."
     ),
    (9, "Anne", "Dodsworth", "Sales Representative", "1966-01-27", "Anne has a BA degree in English from St. Lawrence "
                                                                   "College.  She is fluent in French and German."
     ),

]

# import psycopg2
# from config import host, database, user, password
#
# conn = psycopg2.connect(
#     host="localhost",
#     database="north",
#     user="postgres",
#     password=password
# )
# cur = conn.cursor()
# with open('north_data/employees_data.csv', 'r', encoding="utf-8") as f:
#     next(f)
#     cur.copy_from(f, 'employees', sep=',')
# conn.commit()
# conn.close()

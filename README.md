**RVA City Living Project Proposal**

** **

**1.** 	**Project Title:**

**a.** 	ETL Group Project

** **

**2.** 	**Team Members:**

**a.** 	Edward Gates Jr.

**b.**  	Nikita Jones

**c.** 	Mason Waters

** **

**3.** 	**Project Description Outline:**

** **

<table>
  <tr>
    <td>Project Purpose</td>
    <td>What this project is about and what it aims to accomplish?
We will web-scrape apartment sites in RVA to provide a resource for clients that compare the cost of living and public education by zip code.</td>
  </tr>
  <tr>
    <td>The Need for this Project</td>
    <td>Explain the problem that the project addresses specifically.
Richmond, Virginia, is quickly becoming a city of choice. Many who relocated to RVA are often tasked with searching several sights to gather information that one would need when looking for a residence. This collection of data will be of convenience to those seeking to gather information that would guide an informed decision about what area of RVA best meets their needs.</td>
  </tr>
  <tr>
    <td>Evidence</td>
    <td>What evidence is there to support the need for this project?
To assist users who are in pursuit of reasonably priced living and adequate school ratings. </td>
  </tr>
</table>


 

**4.** 	**EXTRACT** (Objects to Pull):

1. Apartment Data (Apartments.com)

    1. Residence Name

    2. Address Link

    3. Zip Code

    4. Leasing Contact: Phone

    5. Local Education

        1. School Name

        2. Grade Levels

        3. Type: Public or Private

        4. School Number

    6. Starting Price Range

    7. Parking Included

			

2. Population Demographic Data by Zip Code (factfinder.census.gov)

    8. Gender

    9. Age

        5. Citizens of Voting Age (18+)

    10. Race

	 

**5.** 	**TRANSFORM **(data cleaning and transformation)**:**

1. Apartments.com

    1. Used .replace to reassign labels/values to documents

    2. Organized scraped information into a dictionary to be merged with census data

2. Factfinder.census.gov

    3. Pandas

    4. Used Pandas to drop both null values to empty columns,  and renamed columns.

    5. Turned census csv into DataFrame and 

    6. Removed redundant fields, 

    7. Renamed fields, 

    8. Dropped N/A values and 

    9. Converted DataFrame into html table to append dictionary

 

**6.** 	**LOAD **(database/tables/collections):

a.    The final database 

1. "Apartments_db" in MongoDB

b.    Table

1. "Apartments"		

c.      Rationale

1. With there not being a common denominator between the apartment information and the demographic information, a relational database would not be the proper tool to use for our loading process.  Therefore, MongoDB was our best load option

**7.** 	**Rough Breakdown of Tasks:**

a.     Mason Waters

1. Extracted data from Census.gov and  Apartments.com

2. Scraped data from Apartments.com

3. Imported and cleans census csv zip code data

4. Loaded extracted data into MongoDB

b.     Edward Gates Jr. 

1. Cleaned and aggregated data

2. Planned out data that needed to be extracted 	

c.      Nikita Jones

1. Project Manager

2. Extracted data from Apartments.com

3. Created Github Repository

4. Cleaned and aggregated data


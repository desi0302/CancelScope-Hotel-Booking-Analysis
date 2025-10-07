<h1 align="center">CancelScope - Hotel Booking Analysis</h1>

**CancelScope** analyzes hotel booking records to identify the key drivers of reservation cancellations and recommend actions to reduce churn. It combines exploratory data analysis and predictive modeling to produce clear visualisations and an interactive dashboard for hotel managers.


<p align="center">
	<img src="images/dataset-cover-small.png" alt="Dataset cover" width="600" />
</p>

## Dataset Content
* Link to download dataset: [Kaggle Dataset](https://www.kaggle.com/datasets/mathsian/hotel-bookings/data?select=hotel_bookings.csv)
* Data set contains the information on 119,390 hotel bookings between 1st of July of 2015 and the 31st of August 2017
* Both hotels are located in Portugal: the Resort Hotel is in the region of the Algarve and the City Hotel is in the city of Lisbon
* The original raw data set is given in the hotel_bookings.csv file. This is the file that is downloaded for analysis in the current project. It consists of 32 columns


## Business Requirements
* Describe your business requirements


## Hypothesis and how to validate?

* Hypothesis 1: Lead Time vs. Cancellation
- H0: There is no relationship between lead time and the likelihood of booking cancellation.
- H1: Longer lead times are associated with a higher likelihood of booking cancellation.
- Rationale: Customers who book far in advance may have a higher chance of changing their plans or finding alternative options.
- How to Test:chi-square test, compare mean lead time between canceled and non-canceled bookings using a t-test,visualize with boxplots or histograms for canceled vs. non-canceled bookings.

* Hypothesis 2: Deposit Type vs. Cancellation
- H0: Cancellation rates are independent of the type of deposit.
- H1: Bookings with refundable or no deposit have higher cancellation rates than non-refundable deposits.
- Rationale: A higher financial commitment (non-refundable deposit) discourages cancellations, while refundable or no-deposit bookings are easier to cancel.
- How to Test: chi-square test of independence between deposit_type and is_canceled, calculate cancellation rates per deposit type, visualize with a bar chart showing percentage canceled per deposit type.

* Hypothesis 3: Customer Type vs. Cancellation
- H0: Customer type (transient, group, contract, transient_party) does not affect the probability of cancellation.
- H1: Certain customer types (e.g., transient guests) have higher cancellation rates than others (e.g., contract clients).
- Rationale: Groups or contract clients are more committed to their bookings, while individual or transient guests may cancel more frequently.
- How to Test:chi-square test for independence between customer_type_label and is_canceled, compute cancellation rates per customer type,visualize with stacked bar charts to compare cancellation percentages across customer types.

* Hypothesis 4: Family vs. Cancellation
- H0: Being a family booking (is_family) does not affect the likelihood of cancellation.
- H1: Family bookings are less likely to be canceled compared to non-family bookings.
- Rationale: Families often plan stays in advance and are less likely to cancel compared to individual or transient guests.
- How to Test: chi-square test of independence between is_family and is_canceled, calculate cancellation rates for family vs. non-family bookings,visualize with bar plots showing the proportion of cancellations for families vs. non-families.

## Project Plan
* Outline the high-level steps taken for the analysis.
* How was the data managed throughout the collection, processing, analysis and interpretation steps?
* Why did you choose the research methodologies you used?

## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used
* List the data analysis methods used and explain limitations or alternative approaches.
* How did you structure the data analysis techniques. Justify your response.
* Did the data limit you, and did you use an alternative approach to meet these challenges?
* How did you use generative AI tools to help with ideation, design thinking and code optimisation?

## Ethical considerations
* Were there any data privacy, bias or fairness issues with the data?
* How did you overcome any legal or societal issues?

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

## Deployment

## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
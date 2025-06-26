
Verical Parts Data Scraper
This Python script retrieves electronic parts data from Verical.com via their internal API and stores the retrieved information into a CSV file with a timestamped filename.

📌 Features
Sends a POST request to Verical's parametric search API with predefined filters.

Iterates through paginated search results.

Extracts detailed part information such as:

Manufacturer name and ID

Part number (MPN)

Category and description

Prices, datasheet URLs, compliance flags, and more

Saves the data incrementally to a CSV file in the current working directory.

🛠️ Technologies Used
Python 3

requests – for handling HTTP requests

pandas – for structured data storage and manipulation

datetime, os – for file naming and path validation

📄 Output
The script creates a CSV file named like:

نسخ
تحرير
2025_06_26-10_45_03_PM.csv
Each row contains metadata about one part result.

⚙️ How It Works
Sends an initial POST request with part_category_id = 776.

Extracts the total number of results.

Iteratively paginates using start_index parameter.

For each batch of results:

Collects key fields from each part.

Appends data to the CSV file.

🔐 Authentication / Cookies
The script includes headers and previously recorded cookies, but cookie-based authentication is commented out. If the API enforces auth, you may need to refresh cookie values from your browser session or implement login automation.
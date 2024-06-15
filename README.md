# finanlytics
A powerful financial data analysis tool built with Python, Flask, and SQL. Analyze large transactional datasets, identify trends and anomalies, and visualize your findings with interactive plots. 

## Getting Started

### Prerequisites

- Python 3.x installed on your system
- Basic knowledge of virtual environments in Python

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/financial-data-analysis.git
    cd financial-data-analysis
    ```

2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Open your browser** and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

### Managing Your Data

- **Edit the `schema.sql` file** to insert, delete, and edit your financial data. The file contains SQL statements to create the database schema and insert initial data.
- **Run the SQL scripts** using a database client or command line to update your database.


### Customization

- **Templates**: Modify the HTML templates in the `templates` folder to customize the front-end.
- **Static Files**: Add or update images, JavaScript, and CSS in the `static` folder.
- **Database**: Customize and update the database using `schema.sql` and your preferred database client.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


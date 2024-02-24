from flask import Flask, render_template,jsonify, request, redirect, url_for, session
import pyodbc

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Replace connection details with your own

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=AmaanShaik\SQLEXPRESS;'
                      'Database=InfraDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Assuming you have a users table with columns 'username' and 'password'
        username = request.form.get("username")
        password = request.form.get("password")

        # Check the credentials (This is a simple example, not secure for production)
        if username == "sa" and password == "Hussain":
            session['username'] = username  # Store the username in the session
            return redirect(url_for("index"))
        else:
            return render_template("login.html", message="Invalid credentials. Try again.")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    # Check if the user is logged in before rendering the index page
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route("/get_data")
def get_data():
    # Execute your SQL query to get data from the database
    cursor.execute('select LOOKUP_TYPE_ID,LOOKUP_TYPE,TYPE_DESCRIPTION,ENABLED_FLAG,CREATION_DATE,CREATED_BY_USER,LAST_UPDATE_DATE,LAST_UPDATED_BY_USER from Lookup_Type;')
    lookup_type_data = cursor.fetchall()

    cursor.execute('select LOOKUP_VALUE_ID,LOOKUP_TYPE_ID,LOOKUP_CODE,LOOKUP_VALUE,VALUE_DESCRIPTION,ENABLED_FLAG,CREATION_DATE,CREATED_BY_USER,LAST_UPDATE_DATE,LAST_UPDATED_BY_USER from Lookup_Values;')
    lookup_values_data = cursor.fetchall()

    # Format data as HTML for simplicity (you can use JSON for a more structured approach)
    lookup_type_html = "<h2>Lookup Type</h2>"
    lookup_type_html += "<table>\n" 
    lookup_type_html += "<tr>\n" 
    lookup_type_html += "<th>LOOKUP TYPE No</th>\n" 
    lookup_type_html += "<th>LOOKUP TYPE</th>\n" 
    lookup_type_html += "<th>TYPE DESCRIPTION</th>\n"
    lookup_type_html += "<th>ENABLED FLAG</th>\n"
    lookup_type_html += "<th>CREATION DATE</th>\n"
    lookup_type_html += "<th>CREATED BY</th>\n" 
    lookup_type_html += "<th>LAST UPDATE DATE</th>\n" 
    lookup_type_html += "<th>LAST UPDATED BY</th>\n" 
    lookup_type_html += "</tr>\n" 
    for row in lookup_type_data: 
        lookup_type_html += "<tr>\n" 
        lookup_type_html += "<td>{}</td>\n".format(row[0]) 
        lookup_type_html += "<td>{}</td>\n".format(row[1]) 
        lookup_type_html += "<td>{}</td>\n".format(row[2])
        lookup_type_html += "<td>{}</td>\n".format(row[3]) 
        lookup_type_html += "<td>{}</td>\n".format(row[4]) 
        lookup_type_html += "<td>{}</td>\n".format(row[5])
        lookup_type_html += "<td>{}</td>\n".format(row[6]) 
        lookup_type_html += "<td>{}</td>\n".format(row[7]) 
        lookup_type_html += "</tr>\n" 
    lookup_type_html += "</table>"

    lookup_values_html = "<h2>Lookup Values</h2>"
    lookup_values_html += "<table>\n" 
    lookup_values_html += "<tr>\n" 
    lookup_values_html += "<th>LOOKUP VALUE No</th>\n" 
    lookup_values_html += "<th>LOOKUP TYPE No</th>\n" 
    lookup_values_html += "<th>LOOKUP CODE</th>\n"
    lookup_values_html += "<th>LOOKUP VALUE</th>\n"
    lookup_values_html += "<th>VALUE DESCRIPTION</th>\n"
    lookup_values_html += "<th>ENABLED FLAG</th>\n"
    lookup_values_html += "<th>CREATION DATE</th>\n"
    lookup_values_html += "<th>CREATED BY</th>\n" 
    lookup_values_html += "<th>LAST UPDATE DATE</th>\n" 
    lookup_values_html += "<th>LAST UPDATED BY</th>\n" 
    lookup_values_html += "</tr>\n" 
    for row in lookup_values_data: 
        lookup_values_html += "<tr>\n" 
        lookup_values_html += "<td>{}</td>\n".format(row[0]) 
        lookup_values_html += "<td>{}</td>\n".format(row[1]) 
        lookup_values_html += "<td>{}</td>\n".format(row[2])
        lookup_values_html += "<td>{}</td>\n".format(row[3]) 
        lookup_values_html += "<td>{}</td>\n".format(row[4]) 
        lookup_values_html += "<td>{}</td>\n".format(row[5])
        lookup_values_html += "<td>{}</td>\n".format(row[6]) 
        lookup_values_html += "<td>{}</td>\n".format(row[7])
        lookup_values_html += "<td>{}</td>\n".format(row[8]) 
        lookup_values_html += "<td>{}</td>\n".format(row[9]) 
        lookup_values_html += "</tr>\n" 
    lookup_values_html += "</table>"

    return lookup_type_html + lookup_values_html

@app.route("/get_item_data")
def get_item_data():
    cursor.execute('select ITEM_ID, ITEM_NUMBER, ITEM_DESCRIPTION, ITEM_TYPE, MANUFACTURER_CODE, '
                   'ITEM_CATEGORY, CPU, MEMORY, DISKS, UOM, ENABLED_FLAG, CREATION_DATE, CREATED_BY_USER, '
                   'LAST_UPDATE_DATE, LAST_UPDATED_BY_USER from ITEM_MASTER;')
    data = cursor.fetchall()

    # Format data as HTML for simplicity (you can use JSON for a more structured approach)
    html_data = "<table>\n"
    html_data += "<tr>\n"
    html_data += "<th>ITEM No</th>\n"
    html_data += "<th>ITEM NUMBER</th>\n"
    html_data += "<th>ITEM DESCRIPTION</th>\n"
    html_data += "<th>ITEM TYPE</th>\n"
    html_data += "<th>MANUFACTURER CODE</th>\n"
    html_data += "<th>ITEM CATEGORY</th>\n"
    html_data += "<th>CPU</th>\n"
    html_data += "<th>MEMORY</th>\n"
    html_data += "<th>DISKS</th>\n"
    html_data += "<th>UOM</th>\n"
    html_data += "<th>ENABLED FLAG</th>\n"
    html_data += "<th>CREATION DATE</th>\n"
    html_data += "<th>CREATED BY</th>\n"
    html_data += "<th>LAST UPDATE DATE</th>\n"
    html_data += "<th>LAST UPDATED BY</th>\n"
    html_data += "</tr>\n"
    for row in data:
        html_data += "<tr>\n"
        for item in row:
            html_data += "<td>{}</td>\n".format(item)
        html_data += "</tr>\n"
    html_data += "</table>"

    return html_data
# ... (your existing code)

@app.route("/get_inventory_data")
def get_inventory_data():
    # Execute your SQL query to get inventory data from the database
    cursor.execute('select INVENTORY_ID, ITEM_ID, INSTALL_LOCATION, PROJECT_CODE, QUANTITY, IP_ADDRESS, SUBNET_MASK, GATEWAY, COMMENTS, LAST_PO_NUM, LAST_PO_PRICE, RENEWAL_DATE, NOTES, CREATION_DATE, CREATED_BY_USER, LAST_UPDATE_DATE, LAST_UPDATED_BY_USER from Inventory_Onhand;')
    data = cursor.fetchall()

    # Format data as HTML for simplicity (you can use JSON for a more structured approach)
    html_data = "<table>\n"
    html_data += "<tr>\n" 
    html_data += "<th>INVENTORY ID</th>\n" 
    html_data += "<th>ITEM_ID</th>\n" 
    html_data += "<th>INSTALL_LOCATION</th>\n"
    html_data += "<th>PROJECT_CODE</th>\n"
    html_data += "<th>QUANTITY</th>\n"
    html_data += "<th>IP_ADDRESS</th>\n"
    html_data += "<th>SUBNET_MASK</th>\n"
    html_data += "<th>GATEWAY</th>\n"
    html_data += "<th>COMMENTS</th>\n"
    html_data += "<th>LAST_PO_NUM</th>\n"
    html_data += "<th>LAST_PO_PRICE</th>\n"
    html_data += "<th>RENEWAL_DATE</th>\n"
    html_data += "<th>NOTES</th>\n"
    html_data += "<th>CREATION_DATE</th>\n"
    html_data += "<th>CREATED_BY_USER</th>\n"
    html_data += "<th>LAST_UPDATE_DATE</th>\n"
    html_data += "<th>LAST_UPDATED_BY_USER</th>\n"

    html_data += "</tr>\n" 
    for row in data: 
        html_data += "<tr>\n" 
        html_data += "<td>{}</td>\n".format(row[0]) 
        html_data += "<td>{}</td>\n".format(row[1]) 
        html_data += "<td>{}</td>\n".format(row[2])
        html_data += "<td>{}</td>\n".format(row[3])
        html_data += "<td>{}</td>\n".format(row[4])
        html_data += "<td>{}</td>\n".format(row[5])
        html_data += "<td>{}</td>\n".format(row[6])
        html_data += "<td>{}</td>\n".format(row[7])
        html_data += "<td>{}</td>\n".format(row[8])
        html_data += "<td>{}</td>\n".format(row[9])
        html_data += "<td>{}</td>\n".format(row[10])
        html_data += "<td>{}</td>\n".format(row[11])
        html_data += "<td>{}</td>\n".format(row[12])
        html_data += "<td>{}</td>\n".format(row[13])
        html_data += "<td>{}</td>\n".format(row[14])
        html_data += "<td>{}</td>\n".format(row[15])
        html_data += "<td>{}</td>\n".format(row[16])
        html_data += "</tr>\n" 
    html_data += "</table>"

    return html_data

@app.route("/get_purchase_orders")
def get_purchase_orders():
    # Execute your SQL query to get data from the database for PO_HEADER
    cursor.execute('select PO_HEADER_ID, PO_NUMBER, PO_TYPE, PO_DESCRIPTION, VENDOR_NAME, VENDOR_LOCATION, QUOTE_REQUESTED, QUOTE_NUMBER, PO_STATUS, PO_DATE, PO_APPROVED_DATE, PO_APPROVED_BY, PO_REQUESTED, PO_REQUESTED_BY, INVOICE_NUMBER, INVOICE_LINE_NUMBER, INVOICE_AMOUNT, INVOICE_PAID, SUPPORT_START_DATE, SUPPORT_END_DATE, CREATION_DATE, CREATED_BY_USER, LAST_UPDATE_DATE, LAST_UPDATED_BY_USER from PO_HEADER;')
    po_header_data = cursor.fetchall()

    # Execute your SQL query to get data from the database for PO_LINES
    cursor.execute('select PO_LINE_ID, PO_HEADER_ID, PO_LINE_NUMBER, ITEM_ID, PO_LINE_DESCRIPTION, QUANTITY, UNIT_PRICE, LINE_TAX_AMOUNT, SUPPORT_START_DATE, SUPPORT_END_DATE, NEED_BY_DATE, PO_LINE_STATUS, SHIP_LOCATION, INVOICE_NUMBER, INVOICE_LINE_NUMBER, INVOICE_DATE, INVOICE_PAID, INVOICE_AMOUNT, PO_LINE_COMMENTS, CREATION_DATE, CREATED_BY_USER, LAST_UPDATE_DATE, LAST_UPDATED_BY_USER from PO_LINES;')
    po_lines_data = cursor.fetchall()

    # Format data as HTML for simplicity (you can use JSON for a more structured approach)
    po_header_html = "<h2>Purchase Order Header</h2>"
    po_header_html += "<table>\n" 
    po_header_html += "<tr>\n" 
    po_header_html += "<th>PO_HEADER_ID</th>\n" 
    po_header_html += "<th>PO_NUMBER</th>\n" 
    po_header_html += "<th>PO_TYPE</th>\n"
    po_header_html += "<th>PO_DESCRIPTION</th>\n"
    po_header_html += "<th>VENDOR_NAME</th>\n"
    po_header_html += "<th>VENDOR_LOCATION</th>\n"
    po_header_html += "<th>QUOTE_REQUESTED</th>\n"
    po_header_html += "<th>QUOTE_NUMBER</th>\n"
    po_header_html += "<th>PO_STATUS</th>\n"
    po_header_html += "<th>PO_DATE</th>\n"
    po_header_html += "<th>PO_APPROVED_DATE</th>\n"
    po_header_html += "<th>PO_APPROVED_BY</th>\n"
    po_header_html += "<th>PO_REQUESTED</th>\n"
    po_header_html += "<th>PO_REQUESTED_BY</th>\n"
    po_header_html += "<th>INVOICE_NUMBER</th>\n"
    po_header_html += "<th>INVOICE_LINE_NUMBER</th>\n"
    po_header_html += "<th>INVOICE_AMOUNT</th>\n"
    po_header_html += "<th>INVOICE_PAID</th>\n"
    po_header_html += "<th>SUPPORT_START_DATE</th>\n"
    po_header_html += "<th>SUPPORT_END_DATE</th>\n"
    po_header_html += "<th>CREATION_DATE</th>\n"
    po_header_html += "<th>CREATED_BY_USER</th>\n"
    po_header_html += "<th>LAST_UPDATE_DATE</th>\n"
    po_header_html += "<th>LAST_UPDATED_BY_USER</th>\n"
    po_header_html += "</tr>\n" 
    for row in po_header_data: 
        po_header_html += "<tr>\n" 
        po_header_html += "<td>{}</td>\n".format(row[0])
        po_header_html += "<td>{}</td>\n".format(row[1])
        po_header_html += "<td>{}</td>\n".format(row[2])
        po_header_html += "<td>{}</td>\n".format(row[3])
        po_header_html += "<td>{}</td>\n".format(row[4])
        po_header_html += "<td>{}</td>\n".format(row[5])
        po_header_html += "<td>{}</td>\n".format(row[6]) 
        po_header_html += "<td>{}</td>\n".format(row[7]) 
        po_header_html += "<td>{}</td>\n".format(row[8]) 
        po_header_html += "<td>{}</td>\n".format(row[9]) 
        po_header_html += "<td>{}</td>\n".format(row[10]) 
        po_header_html += "<td>{}</td>\n".format(row[11]) 
        po_header_html += "<td>{}</td>\n".format(row[12]) 
        po_header_html += "<td>{}</td>\n".format(row[13]) 
        po_header_html += "<td>{}</td>\n".format(row[14]) 
        po_header_html += "<td>{}</td>\n".format(row[15]) 
        po_header_html += "<td>{}</td>\n".format(row[16]) 
        po_header_html += "<td>{}</td>\n".format(row[17]) 
        po_header_html += "<td>{}</td>\n".format(row[18]) 
        po_header_html += "<td>{}</td>\n".format(row[19]) 
        po_header_html += "<td>{}</td>\n".format(row[20]) 
        po_header_html += "<td>{}</td>\n".format(row[21]) 
        po_header_html += "<td>{}</td>\n".format(row[22]) 
        po_header_html += "<td>{}</td>\n".format(row[23]) 
        po_header_html += "</tr>\n" 
    po_header_html += "</table>"

    po_lines_html = "<h2>Purchase Order Lines</h2>"
    po_lines_html += "<table>\n" 
    po_lines_html += "<tr>\n" 
    po_lines_html += "<th>PO_LINE_ID</th>\n" 
    po_lines_html += "<th>PO_HEADER_ID</th>\n" 
    po_lines_html += "<th>PO_LINE_NUMBER</th>\n"
    po_lines_html += "<th>ITEM_ID</th>\n"
    po_lines_html += "<th>PO_LINE_DESCRIPTION</th>\n"
    po_lines_html += "<th>QUANTITY</th>\n"
    po_lines_html += "<th>UNIT_PRICE</th>\n"
    po_lines_html += "<th>LINE_TAX_AMOUNT</th>\n"
    po_lines_html += "<th>SUPPORT_START_DATE</th>\n"
    po_lines_html += "<th>SUPPORT_END_DATE</th>\n"
    po_lines_html += "<th>NEED_BY_DATE</th>\n"
    po_lines_html += "<th>PO_LINE_STATUS</th>\n"
    po_lines_html += "<th>SHIP_LOCATION</th>\n"
    po_lines_html += "<th>INVOICE_NUMBER</th>\n"
    po_lines_html += "<th>INVOICE_LINE_NUMBER</th>\n"
    po_lines_html += "<th>INVOICE_DATE</th>\n"
    po_lines_html += "<th>INVOICE_PAID</th>\n"
    po_lines_html += "<th>INVOICE_AMOUNT</th>\n"
    po_lines_html += "<th>PO_LINE_COMMENTS</th>\n"
    po_lines_html += "<th>CREATION_DATE</th>\n"
    po_lines_html += "<th>CREATED_BY_USER</th>\n"
    po_lines_html += "<th>LAST_UPDATE_DATE</th>\n"
    po_lines_html += "<th>LAST_UPDATED_BY_USER</th>\n"
    po_lines_html += "</tr>\n" 
    for row in po_lines_data: 
        po_lines_html += "<tr>\n" 
        po_lines_html += "<td>{}</td>\n".format(row[0]) 
        po_lines_html += "<td>{}</td>\n".format(row[1]) 
        po_lines_html += "<td>{}</td>\n".format(row[2])
        po_lines_html += "<td>{}</td>\n".format(row[3]) 
        po_lines_html += "<td>{}</td>\n".format(row[4]) 
        po_lines_html += "<td>{}</td>\n".format(row[5])
        po_lines_html += "<td>{}</td>\n".format(row[6]) 
        po_lines_html += "<td>{}</td>\n".format(row[7]) 
        po_lines_html += "<td>{}</td>\n".format(row[8]) 
        po_lines_html += "<td>{}</td>\n".format(row[9]) 
        po_lines_html += "<td>{}</td>\n".format(row[10]) 
        po_lines_html += "<td>{}</td>\n".format(row[11]) 
        po_lines_html += "<td>{}</td>\n".format(row[12]) 
        po_lines_html += "<td>{}</td>\n".format(row[13]) 
        po_lines_html += "<td>{}</td>\n".format(row[14]) 
        po_lines_html += "<td>{}</td>\n".format(row[15]) 
        po_lines_html += "<td>{}</td>\n".format(row[16]) 
        po_lines_html += "<td>{}</td>\n".format(row[17]) 
        po_lines_html += "<td>{}</td>\n".format(row[18]) 
        po_lines_html += "<td>{}</td>\n".format(row[19]) 
        po_lines_html += "<td>{}</td>\n".format(row[20]) 
        po_lines_html += "<td>{}</td>\n".format(row[21]) 
        po_lines_html += "<td>{}</td>\n".format(row[22]) 
        po_lines_html += "</tr>\n" 
    po_lines_html += "</table>"

    return po_header_html + po_lines_html



if __name__ == '__main__':
    app.run(debug=True)

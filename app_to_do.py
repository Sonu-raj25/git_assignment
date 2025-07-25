























@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('item_name')
    item_desc = request.form.get('item_desc')

    if item_name and item_desc:
        collection.insert_one({
            "item_name": item_name,
            "item_desc": item_desc
        })
        print(f"Item Name: {item_name}, Item Description: {item_desc}")
        return "Item added successfully!"
    else:
        return "Missing data", 400



if __name__ == '__main__':
    app.run(debug=True)




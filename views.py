contact_list_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact List</title>
</head>
<body style="width:50%;height:50%;font-family: Arial, sans-serif;margin: auto;padding: 0;background-color: #f4f4f4;">
    <h1 style="color: #333;">Contact List</h1>
    <ul style="list-style: none; padding: 0;">
    {contacts}
    </ul>
    <hr>
    <h2 style="color: #333;">Create New Contact</h2>
    <form style="margin-top: 10px;" action="/create" method="post">
        Name: <input style="width: 100%;padding: 5px;margin-bottom: 10px;" type="text" name="name" required><br>
        Email: <input style="width: 100%;padding: 5px;margin-bottom: 10px;" type="text" name="email" required><br>
        Phone: <input style="width: 100%;padding: 5px;margin-bottom: 10px;" type="text" name="phone" required><br>
        <input style="background-color: #007bff;color: #fff;border: none;padding: 5px 10px;cursor: pointer;border-radius: 5px;" type="submit" value="Create">
    </form>
</body>
</html>
"""

contact_template = """
<li style="background-color: #fff;margin: 0;padding: 10px;border: 1px solid #ddd;border-radius: 5px;">
    <strong style="display:inline-block;margin: 5px 0;padding:0">Name:</strong> {name}<br>
    <strong style="display:inline-block;margin: 5px 0;padding:0">Email:</strong> {email}<br>
    <strong style="display:inline-block;margin: 5px 0;padding:0">Phone:</strong> {phone}<br>
    <div style="display: flex;max-width:15%;justify-content: space-between; align-items: center;">
        <form action="/edit/{index}" method="get">
            <button style="background-color: #007bff;color: #fff;border: none;padding: 5px 10px;cursor: pointer;border-radius: 5px;">Edit</button>
        </form>
        <form action="/delete/{index}" method="post">
            <button style="background-color: #007bff;color: #fff;border: none;padding: 5px 10px;cursor: pointer;border-radius: 5px;">Delete</button>
        </form>
    </div>
</li>
"""

edit_contact_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Edit Contact</title>
</head>
<body style="width:50%;height:50%;font-family: Arial, sans-serif;margin: auto;padding: 0;background-color: #f4f4f4;">
    <h1 style="color: #333;">Edit Contact</h1>
    <form action="/update/{index}" method="post" style="background-color: #fff;margin: 10px;padding: 10px;border: 1px solid #ddd;border-radius: 5px;">
        Name: <input style="width: 100%;padding: 5px 0 0 5px;margin:0 15px 15px 0;" type="text" name="name" value="{name}"><br>
        Email: <input style="width: 100%;padding: 5px 0 0 5px;margin:0 15px 15px 0;" type="text" name="email" value="{email}"><br>
        Phone: <input style="width: 100%;padding: 5px 0 0 5px;margin:0 15px 15px 0" type="text" name="phone" value="{phone}"><br>
        <input style="background-color: #007bff;color: #fff;border: none;padding: 5px 10px;cursor: pointer;border-radius: 5px;" type="submit" value="Update">
    </form>
</body>
</html>
"""

error_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
    <script>setTimeout(function() {{window.location.href = '/';}}, 5000);</script>
</head>
<body style="width: 50%;height: 50%;margin:auto;font-family: Arial, sans-serif; padding: 0; background-color: #f4f4f4;">
    <h1 style="color: #333;">Error</h1>
    <p style="color: #f00">{error_message}</p>
    <p style="color: #f00">Redirecting to homepage...</p>
</body>
</html>
"""

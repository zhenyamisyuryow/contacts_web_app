from jinja2 import Environment, FileSystemLoader

class ContactView:
    @staticmethod
    def render_template(template_name:str, **kwargs):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template(template_name)
        if not kwargs:
            return template.render()
        html = template.render(kwargs if kwargs else None)
        return html

    @staticmethod
    def success_message():
        message = """
                    <script>
                        alert('Success! Redirecting to the homepage');
                        window.location.href = '/';
                    </script>
                """
        return message
    
    
    @staticmethod
    def warning_message(message:str, location:str):
        output = f"""
                    <script>
                        alert('{message}');
                        window.location.href = '{location}';
                    </script>
        """
        return output
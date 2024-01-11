from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views import View
import json
import matplotlib
matplotlib.use('Agg')  # Set the backend to Agg (Agg is a non-interactive backend)

import matplotlib.pyplot as plt
import io
import base64

class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get(self, request):
        # Read numbers from the score.txt file
        numbers = self.read_numbers_from_file("E:/MOD 3/CIS 403/TEST/shop/static/shop/styles/score.txt")
        context = {
            "numbers": numbers,
            "plot": self.generate_plot(numbers),
        }
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))

    def read_numbers_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                # Read numbers from the file and convert them to integers
                numbers = [int(line.strip()) for line in file.readlines()]
            return numbers
        except FileNotFoundError:
            return []  # Return an empty list if the file is not found

    def generate_plot(self, numbers):
        # Set the backend to Agg
        plt.switch_backend('Agg')

        # Create a new figure and axis
        fig, ax = plt.subplots()

        # Create a line chart
        ax.plot(range(1, len(numbers) + 1), numbers, label='Scores')

        # Add labels and title
        ax.set_xlabel('Games')
        ax.set_ylabel('Scores')
        ax.set_title('Scores Over Time')

        # Add legend
        ax.legend()

        # Convert the plot to base64 for embedding in HTML
        image_stream = io.BytesIO()
        fig.savefig(image_stream, format='png')
        image_stream.seek(0)
        encoded_image = base64.b64encode(image_stream.read()).decode('utf-8')
        plt.close(fig)

        return f'data:image/png;base64,{encoded_image}'


class ClearScoresView(View):
    def get(self, request, *args, **kwargs):
        # Implement logic to clear scores (overwrite the score.txt file with an empty list)
        try:
            file_path = "E:/MOD 3/CIS 403/TEST/shop/static/shop/styles/score.txt"
            with open(file_path, "w") as file:
                file.truncate(0)
            return JsonResponse({'message': 'Scores cleared successfully'})
        except Exception as e:
            return JsonResponse({'message': f'Error clearing scores: {str(e)}'})

class GetScoresView(View):
    def get(self, request):
        # Replace this path with the actual path to your score.txt file
        file_path = "E:/MOD 3/CIS 403/TEST/shop/static/shop/styles/score.txt"

        try:
            with open(file_path, "r") as file:
                # Read numbers from the file and convert them to integers
                scores = [int(line.strip()) for line in file.readlines()]
            return JsonResponse({"scores": scores})
        except FileNotFoundError:
            return JsonResponse({"scores": []})
def get_nav_bar_to_context(request):
    return {
        'nav_bar': [
            {
                'name': 'Home',
                'link': '../'
            },
            {
                'name': 'News',
                'link': '../news'
            },
            {
                'name': 'Authors',
                'link': '../authors'
            },
            {
                'name': 'Swagger',
                'link': '../swagger'
            }
        ]
    }
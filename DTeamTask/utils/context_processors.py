def get_nav_bar_to_context(request):
    return {
        'nav_bar': [
            {
                'name': 'Home',
                'link': '../home'
            },
            {
                'name': 'News',
                'link': '../news'
            }
        ]
    }
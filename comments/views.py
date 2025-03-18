from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Comment

@login_required
def add_comment(request, content_type_id, object_id):
    if request.method == 'POST':
        text = request.POST.get('comment_text')
        # Get the content type instance
        content_type = get_object_or_404(ContentType, id=content_type_id)
        Comment.objects.create(
            user=request.user,
            content_type=content_type,
            object_id=object_id,
            text=text
        )
    return redirect_to_object(content_type_id, object_id)

@login_required
def reply_comment(request, comment_id):
    if request.method == 'POST':
        parent_comment = get_object_or_404(Comment, id=comment_id)
        text = request.POST.get('reply_text')
        Comment.objects.create(
            user=request.user,
            content_type=parent_comment.content_type,
            object_id=parent_comment.object_id,
            text=text,
            parent=parent_comment
        )
    return redirect_to_object(parent_comment.content_type.id, parent_comment.object_id)

def redirect_to_object(content_type_id, object_id):
    from django.shortcuts import redirect
    content_type = get_object_or_404(ContentType, id=content_type_id)
    model_class = content_type.model_class()
    instance = get_object_or_404(model_class, id=object_id)
    if hasattr(instance, 'get_absolute_url'):
        return redirect(instance.get_absolute_url())
    return redirect('/')

## populate_latest_resource_edit.py installtion

to make this function work add
```
 if LatestResourceEdit.objects.filter(resourceinstanceid=self.resourceinstance.resourceinstanceid, edittype = 'create').exists():
            if LatestResourceEdit.objects.filter(resourceinstanceid = self.resourceinstance.resourceinstanceid).exclude(edittype = 'create').exists():
                LatestResourceEdit.objects.filter(resourceinstanceid = self.resourceinstance.resourceinstanceid).exclude(edittype = 'create').delete()
            #Delete old versions and add latest edit
            latest_edit = LatestResourceEdit()
            latest_edit.resourceinstanceid = self.resourceinstance.resourceinstanceid
            latest_edit.timestamp = timestamp
            latest_edit.user_username = getattr(user, "username", "")
            latest_edit.edittype = edit_type
            latest_edit.save()

        else:
            latest_edit = LatestResourceEdit()
            latest_edit.resourceinstanceid = self.resourceinstance.resourceinstanceid
            latest_edit.timestamp = timestamp
            latest_edit.edittype = edit_type
            latest_edit.user_username = getattr(user,"username", "")
            latest_edit.resourcedisplayname =  Resource.objects.get(resourceinstanceid=self.resourceinstance.resourceinstanceid).displayname
            latest_edit.save()
```
at the bottom of `def save_edit()` in `tile.py` located in `app/models/tile.py'

then add 
```
class LatestResourceEdit(models.Model):
    editlogid = models.UUIDField(primary_key=True, default=uuid.uuid1)
    resourceinstanceid = models.TextField(blank=True, null=True)
    resourcedisplayname = models.TextField(blank=True, null=True)
    edittype = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    user_username = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = "latest_resource_edit"
```
just after `EditLog()` in `models.py` located in `app/models/tile.py`

and finally add
```
if LatestResourceEdit.objects.filter(resourceinstanceid=self.resourceinstanceid, edittype = 'create').exists():
            if LatestResourceEdit.objects.filter(resourceinstanceid = self.resourceinstanceid).exclude(edittype = 'create').exists():
                LatestResourceEdit.objects.filter(resourceinstanceid = self.resourceinstanceid).exclude(edittype = 'create').delete()
            #Delete old verions and add latest edit
            latest_edit = LatestResourceEdit()
            latest_edit.resourceinstanceid = self.resourceinstanceid
            latest_edit.timestamp = timestamp
            latest_edit.user_username = getattr(user, "username", "")
            latest_edit.edittype = edit_type
            latest_edit.resourcedisplayname =  Resource.objects.get(resourceinstanceid=self.resourceinstanceid).displayname
            latest_edit.save()

        else:
            latest_edit = LatestResourceEdit()
            latest_edit.resourceinstanceid = self.resourceinstanceid
            latest_edit.timestamp = timestamp
            latest_edit.edittype = edit_type
            latest_edit.user_username = getattr(user,"username", "")
            latest_edit.resourcedisplayname =  Resource.objects.get(resourceinstanceid=self.resourceinstanceid).displayname
            latest_edit.save()
```
 at the bottom of `def save_edits()` to `resource.py` located in `app/models/tile.py`

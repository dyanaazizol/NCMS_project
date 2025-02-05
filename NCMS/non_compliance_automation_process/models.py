from django.db import models

# Model for Division
class Division(models.Model):
    division_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# Model for Doer
class Doer(models.Model):
    doer_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    doer_email = models.EmailField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    direct_supervisor = models.CharField(max_length=100)
    gm_hod = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    subsidiary = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    vertical = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# Model for DCC
class DCC(models.Model):
    dcc_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    dcc_email = models.EmailField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Model for Process Owner
class ProcessOwner(models.Model):
    po_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Policy Procedure
class PolicyProcedure(models.Model):
    policy_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    process_owner = models.ForeignKey(ProcessOwner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Model for Scenario
class Scenario(models.Model):
    scenario_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    policy = models.ForeignKey(PolicyProcedure, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Model for BGCM
class BGCM(models.Model):
    bgcm_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    bgcm_email = models.EmailField()
    bgcm_division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Model for HCBD
class HCBD(models.Model):
    hcbd_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    hcbd_email = models.EmailField()
    hcbd_division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Model for level
class Level(models.Model):
    level_id = models.CharField(max_length=20, primary_key=True)

# Model for action
class Action(models.Model):
    action_id = models.CharField(max_length=20, primary_key=True)
    action_details = models.TextField(max_length=300)
    levelID = models.ForeignKey(Level, on_delete=models.CASCADE)

# Model for nc rating
class Rate(models.Model):
    rate_id = models.CharField(max_length=20, primary_key=True)
    actionID = models.ForeignKey(Action, on_delete=models.CASCADE)

# Model for NCReport
class NCReport(models.Model):
    dccID = models.ForeignKey(DCC, on_delete=models.CASCADE)
    doerID = models.ForeignKey(Doer, on_delete=models.CASCADE)
    scenarioID = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255, default='Policy')
    process_owner = models.CharField(max_length=255, default='Process Owner')
    dateIncident = models.DateField()
    typeRef = models.TextField()
    refNo = models.TextField()
    conProjectName = models.TextField()
    accName = models.TextField()
    poDivision = models.TextField()
    scenarioDetails = models.TextField()
    catJus = models.TextField()
    poFI = models.TextField()
    nonFI = models.TextField()
    frequency = models.TextField()
    rateID =  models.ForeignKey(Rate, on_delete=models.CASCADE)
    level = models.CharField(max_length=255, default='pending..')
    doerJustification = models.TextField(default="pending..")
    remarksBGCM = models.TextField(default="pending..")
    remarksHCBD = models.TextField(default="pending..")
    clarificationDate = models.TextField(default="pending..") 
    ncDecision = models.TextField(default="pending..")
    remarksPO = models.TextField(default="pending..")
    action = models.TextField(default="pending..")
    acknowledgment = models.TextField(default="pending..")
    status = models.TextField(default="pending..")

    def str(self):
        return f"NC Report {self.id} by {self.doerID.name}"
    
# Model for Admin
class Admin(models.Model):
    admin_id = models.CharField(max_length=20, primary_key = True)
    admin_name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    admin_email = models.EmailField()


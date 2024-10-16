from django.urls import path
from. import views

urlpatterns = [

    # login page
    path('', views.login, name='login'),

    ###################################### doer ############################################################################
    path('doerHomepage/', views.doerHomepage, name='doerHomepage'),

        # doer search nc
        path('doerHomepage/doerSearchNC/', views.doerSearchNC, name='doerSearchNC'),
        # doer acknowledge
        path('doerHomepage/doerSearchNC/approve/<int:report_id>/', views.approve_acknowledgement, name='acknowledge'),
            # doer view nc
            path('doerHomepage/doerSearchNC/doerViewNC/<str:report_id>/', views.doerViewNC, name='doerViewNC'),

    path('doerHomepage/doerProfile/', views.doerProfile, name='doerProfile'),

    ###################################### dcc ############################################################################
    path('dccHomepage/', views.dccHomepage, name='dccHomepage'),
    path('dccHomepage/dccAction/', views.dccAction, name='dccAction'),
    path('dccHomepage/dccAction/dccAdddoer/', views.dccAdddoer, name='dccAdddoer'),
    path('dccHomepage/dccAction/dccChooseNC/', views.dccChooseNC, name='dccChooseNC'),

        # dcc search nc
        path('dccHomepage/dccAction/dccChooseNC/dccSearchNC', views.dccSearchNC, name='dccSearchNC'),
        # dcc export excel
        path('dccHomepage/dccAction/dccChooseNC/dccSearchNC/exportExcel/', views.exportExcel, name='exportExcel'),
            # dcc view nc
            path('dccHomepage/dccAction/dccChooseNC/dccSearchNC/dccViewNC/<str:report_id>/', views.dccViewNC, name='dccViewNC'),
            # dcc delete nc
            path('dccHomepage/dccAction/dccChooseNC/dccSearchNC/delete/<int:report_id>/', views.delete_Report, name='deleteReport'),

        # dcc create nc
        path('dccHomepage/dccAction/dccChooseNC/dccCreateNC', views.dccCreateNC, name='dccCreateNC'),
            # dcc choose scenario
            path('get-scenario-details/', views.get_scenario_details, name='get_scenario_details'),
            path('get-ncRating-details/', views.get_ncRating_details, name='get_ncRating_details'),
        
    path('dccHomepage/dccProfile/', views.dccProfile, name='dccProfile'),
        

    ###################################### BGCM ############################################################################
    path('BGCMHomepage/', views.BGCMHomepage, name='BGCMHomepage'),

        # bgcm search nc
        path('BGCMHomepage/BGCMSearchNC/', views.BGCMSearchNC, name='BGCMSearchNC'),
        # bgcm view nc
        path('BGCMHomepage/BGCMSearchNC/BGCMViewNC/<str:report_id>/', views.BGCMViewNC, name='BGCMViewNC'),


    path('BGCMHomepage/BGCMProfile/', views.BGCMProfile, name='BGCMProfile'),
    

    ###################################### HCBD ############################################################################
    path('HCBDHomepage/', views.HCBDHomepage, name='HCBDHomepage'),

        # HCBD search nc
        path('HCBDHomepage/HCBDSearchNC/', views.HCBDSearchNC, name='HCBDSearchNC'),
        # HCBD view nc
        path('HCBDHomepage/HCBDSearchNC/HCBDViewNC/<str:report_id>/', views.HCBDViewNC, name='HCBDViewNC'),

    path('HCBDHomepage/HCBDProfile/', views.HCBDProfile, name='HCBDProfile'),

    ###################################### Admin ############################################################################
    
    path('AdminHomepage/', views.AdminHomepage, name='AdminHomepage'),
    path('AdminHomepage/AdminManage/', views.AdminManage, name='AdminManage'),

        # Admin choose DCC
        path('AdminHomepage/AdminManage/AdminManageDCC/', views.AdminManageDCC, name='AdminManageDCC'),
            # Admin add DCC
            path('AdminHomepage/AdminManage/AdminManageDCC/AdminaddDCC', views.AdminaddDCC, name='AdminaddDCC'),
            # Admin search DCC
            path('AdminHomepage/AdminManage/AdminManageDCC/AdminSearchDCC/', views.AdminSearchDCC, name='AdminSearchDCC'),
                # Admin delete DCC
                path('AdminHomepage/AdminManage/AdminManageDCC/AdminSearchDCC/AdminDeleteDCC/<str:dcc_id>/', views.AdminDeleteDCC, name='AdminDeleteDCC'),
                # Admin Update DCC
                path('AdminHomepage/AdminManage/AdminManageDCC/AdminSearchDCC/AdminUpdateDCC/<str:dcc_id>/', views.AdminUpdateDCC, name='AdminUpdateDCC'),

        # Admin choose BGCM
        path('AdminHomepage/AdminManage/AdminManageBGCM/', views.AdminManageBGCM, name='AdminManageBGCM'),
            # Admin add BGCM
            path('AdminHomepage/AdminManage/AdminManageDCC/AdminaddBGCM', views.AdminaddBGCM, name='AdminaddBGCM'),
            # Admin Search BGCM
            path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchBGCM/', views.AdminSearchBGCM, name='AdminSearchBGCM'),
                # Admin Delete BGCM
                path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchBGCM/AdminDeleteBGCM/<str:bgcm_id>/', views.AdminDeleteBGCM, name='AdminDeleteBGCM'),
                # Admin Update BGCM
                path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchBGCM/AdminUpdateBGCM/<str:bgcm_id>/', views.AdminUpdateBGCM, name='AdminUpdateBGCM'),
    
        # Admin choose HCBD
        path('AdminHomepage/AdminManage/AdminManageHCBD/', views.AdminManageHCBD, name='AdminManageHCBD'),
            # Admin add HCBD
            path('AdminHomepage/AdminManage/AdminManageDCC/AdminaddHCBD', views.AdminaddHCBD, name='AdminaddHCBD'),
            # Admin Search HCBD
            path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchHCBD/', views.AdminSearchHCBD, name='AdminSearchHCBD'),
                # Admin Delete HCBD
                path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchBGCM/AdminDeleteHCBD/<str:hcbd_id>/', views.AdminDeleteHCBD, name='AdminDeleteHCBD'),
                # Admin Update HCBD
                path('AdminHomepage/AdminManage/AdminManageBGCM/AdminSearchBGCM/AdminUpdateHCBD/<str:hcbd_id>/', views.AdminUpdateHCBD, name='AdminUpdateHCBD'),
    
    path('AdminHomepage/AdminProfile/', views.AdminProfile, name='AdminProfile'),
    
]

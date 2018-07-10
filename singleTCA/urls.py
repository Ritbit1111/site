from django.conf.urls import url, include
import singleTCA.views as vw

urlpatterns = [
         url(r'^$', vw.date_acc_view),
         url(r'^tcaform$', vw.date_acc_view),
         url(r'^portfolio_list$', vw.portfolio_view),
         url(r'^instruments_list$', vw.instrument_view),
         url(r'^summary$', vw.summary_view),
         url(r'^download$', vw.download),
]
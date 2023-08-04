from django.shortcuts import render

from erp_demo.custom_logic.custom_prototypes import PrototypeViews
from erp_demo.newactions_mng.models import NewAction
from erp_demo.nonconformity_mng.models import ContainmentToActions, CorrectionToActions, \
    PermanentToActions, SystematicToActions
from erp_demo.opportunity_mng.models import OpportunitiesToActions
from erp_demo.risk_mng.models import RisksToActions


class NewActionsMngViews(PrototypeViews):
    def actions_matrix(self, request):
        self._empty_context()

        # updated
        # ---------------------------------------------------------------------------------------

        try:
            all_actions = NewAction.objects.all()
        except NewAction.DoesNotExist:
            return render(request, 'error.html', {'error_message': f"{NewAction} not found."})
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

        all_actions_dict = {}
        for action in all_actions:
            try:
                action_risks = RisksToActions.objects.filter(action_id=action).prefetch_related('risk_id')
                action_opportunities = OpportunitiesToActions.objects.filter(action_id=action).prefetch_related(
                    'opportunity_id')
                action_nonconformities = list(
                    ContainmentToActions.objects.filter(action_id=action).prefetch_related('nonconformity_id')) + \
                                         list(CorrectionToActions.objects.filter(action_id=action).prefetch_related(
                                             'nonconformity_id')) + \
                                         list(PermanentToActions.objects.filter(action_id=action).prefetch_related(
                                             'nonconformity_id')) + \
                                         list(SystematicToActions.objects.filter(action_id=action).prefetch_related(
                                             'nonconformity_id'))
            except Exception as e:
                print(f"Unexpected error: {e}")
                return render(request, 'error.html', {'error_message': f'An unexpected error occurred: {e}.'})

            all_actions_dict[action] = {
                'risks': [relation.risk_id for relation in action_risks],
                'opportunities': [relation.opportunity_id for relation in action_opportunities],
                'nonconformities': list(set([relation.nonconformity_id for relation in action_nonconformities])),
            }

        self.context['all_objects'] = self._main_object_queryset(request)
        self.context['all_actions_dict'] = all_actions_dict

        try:
            return render(request, 'newactions_mng/newactions_matrix.html', self.context)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return render(request, 'error.html',
                          {'error_message': f'An unexpected error occurred: {e}.'})

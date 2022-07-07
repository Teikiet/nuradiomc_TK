"""
Simple, barebones simulation class
"""
import NuRadioReco.modules.trigger.highLowThreshold
import NuRadioReco.modules.trigger.simpleThreshold
import NuRadioReco.modules.channelBandPassFilter
from NuRadioReco.utilities import units
from NuRadioMC.simulation import simulation
"""
simple_threshold = simpleThreshold.triggerSimulator()


class Simulation(simulation.simulation):
    def _detector_simulation_filter_amp(self, evt, station, det):
        pass

    def _detector_simulation_trigger(self, evt, station, det):
        simple_threshold.run(
            evt=self._evt,
            station=self._station,
            det=self._det,
            threshold=4 * self._Vrms,
            number_concidences=3,
            trigger_name="simple_threshold",
        )

"""
# initialize detector sim modules
simpleThreshold = NuRadioReco.modules.trigger.simpleThreshold.triggerSimulator()
highLowThreshold = NuRadioReco.modules.trigger.highLowThreshold.triggerSimulator()
channelBandPassFilter = NuRadioReco.modules.channelBandPassFilter.channelBandPassFilter()

class Simulation(simulation.simulation):

    def _detector_simulation_filter_amp(self, evt, station, det):
        channelBandPassFilter.run(evt, station, det, passband=[80 * units.MHz, 1000 * units.GHz],
                                  filter_type='butter', order=2)
        channelBandPassFilter.run(evt, station, det, passband=[0, 500 * units.MHz],
                                  filter_type='butter', order=10)

    def _detector_simulation_trigger(self, evt, station, det):
        # first run a simple threshold trigger
        simpleThreshold.run(evt, station, det,
                             threshold=3 * self._Vrms,
                             triggered_channels=None,  # run trigger on all channels
                             number_concidences=1,
                             trigger_name='simple_threshold')  # the name of the trigger

        # run a high/low trigger on the 4 downward pointing LPDAs
        highLowThreshold.run(evt, station, det,
                                    threshold_high=4 * self._Vrms,
                                    threshold_low=-4 * self._Vrms,
                                    triggered_channels=[0, 1, 2, 3],  # select the LPDA channels
                                    number_concidences=2,  # 2/4 majority logic
                                    trigger_name='LPDA_2of4_4.1sigma',
                                    set_not_triggered=(not station.has_triggered("simple_threshold")))  # calculate more time consuming ARIANNA trigger only if station passes simple trigger

        # run a high/low trigger on the 4 surface dipoles
        highLowThreshold.run(evt, station, det,
                                    threshold_high=3 * self._Vrms,
                                    threshold_low=-3 * self._Vrms,
                                    triggered_channels=[4, 5, 6, 7],  # select the bicone channels
                                    number_concidences=4,  # 4/4 majority logic
                                    trigger_name='surface_dipoles_4of4_3sigma',
                                    set_not_triggered=(not station.has_triggered("simple_threshold")))  # calculate more time consuming ARIANNA trigger only if station passes simple trigger

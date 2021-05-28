# cspell:ignore tolist
from pprint import pprint
from typing import Sequence

import numpy as np
import pytest
from ampform.data import EventCollection
from ampform.kinematics import ReactionInfo
from qrules.particle import ParticleCollection

from tensorwaves.data import generate_phsp
from tensorwaves.data.phasespace import TFUniformRealNumberGenerator


def test_generate_data(data_sample: EventCollection):
    sample_size = 5
    sub_sample = data_sample.select_events(slice(0, sample_size))
    print("Expected values, get by running pytest with the -s flag")
    pprint(
        {
            i: np.round(four_momenta, decimals=11).tolist()
            for i, four_momenta in sub_sample.items()
        }
    )
    expected_sample = {
        0: [
            [1.49284684902, -0.84790794373, -1.19744015271, -0.27528333452],
            [1.51776423337, 0.32069821964, 0.14217675404, 1.47666742723],
            [1.40159883808, -0.99512636301, 0.97912902345, -0.1245358582],
            [1.53448630943, 0.20082048169, 0.15757370698, -1.51310604216],
            [1.45111676561, 0.54809208465, 1.12645968459, -0.73240938904],
        ],
        1: [
            [1.35290167494, 0.86789927359, 1.01492686264, 0.16970126666],
            [0.88914805719, -0.19071913356, 0.08713876399, -0.85346269922],
            [0.76423429742, 0.15644538516, -0.65782537005, 0.32958450934],
            [0.69736757037, -0.04948850316, -0.10956533074, 0.67353479347],
            [1.46945697438, -0.63259191506, -1.06583460163, 0.77775904623],
        ],
        2: [
            [0.25115147603, -0.01999132986, 0.18251329007, 0.10558206786],
            [0.68998770944, -0.12997908608, -0.22931551803, -0.62320472801],
            [0.9310668645, 0.83868097785, -0.32130365341, -0.20504865113],
            [0.8650461202, -0.15133197854, -0.04800837624, 0.83957124869],
            [0.17632626001, 0.08449983041, -0.06062508296, -0.04534965719],
        ],
    }
    assert sub_sample.n_events == EventCollection(expected_sample).n_events
    assert set(sub_sample) == set(expected_sample)
    for i, momenta in sub_sample.items():
        assert pytest.approx(momenta) == expected_sample[i]


@pytest.mark.parametrize(
    ("initial_state", "final_state", "expected_sample"),
    [
        (
            "J/psi(1S)",
            ("pi0", "pi0", "pi0"),
            EventCollection(
                {
                    0: [
                        [0.841233472, 0.799667989, 0.159823862, 0.156340839],
                        [0.640234742, -0.364360112, -0.371962329, 0.347228344],
                        [0.631540320, 0.403805561, 0.417294074, -0.208401449],
                    ],
                    1: [
                        [1.09765205, -0.05378975, -0.53523771, -0.94723204],
                        [1.426564296, 1.168326711, -0.060296302, -0.805136016],
                        [1.243480165, 0.014812643, 0.081738919, 1.233338364],
                    ],
                    2: [
                        [1.158014477, -0.745878234, 0.375413844, 0.790891204],
                        [1.030100961, -0.803966599, 0.432258632, 0.457907671],
                        [1.22187951, -0.41861820, -0.49903210, -1.02493691],
                    ],
                }
            ),
        ),
        (
            "J/psi(1S)",
            ("pi0", "pi0", "pi0", "gamma"),
            EventCollection(
                {
                    0: [
                        [0.520913076, 0.037458949, 0.339629143, -0.369297399],
                        [1.180624927, -0.569078090, 0.687702756, -0.760836072],
                        [0.606831154, 0.543652274, 0.220242315, -0.077206475],
                    ],
                    1: [
                        [0.353305116, 0.130561009, 0.299006221, -0.012444727],
                        [0.194507152, 0.123009165, 0.057692537, 0.033979586],
                        [0.331482507, 0.224048290, -0.156048645, 0.130817046],
                    ],
                    2: [
                        [1.276779728, 0.236609937, -0.366594420, 1.192296945],
                        [1.339317905, 0.571746863, -0.586304492, 1.051145223],
                        [0.820720580, 0.402982692, -0.697161285, 0.083274400],
                    ],
                    3: [
                        [0.945902080, -0.40462990, -0.27204094, -0.81055482],
                        [0.38245001, -0.12567794, -0.15909080, -0.32428874],
                        [1.337865758, -1.170683257, 0.632967615, -0.136884971],
                    ],
                }
            ),
        ),
        (
            "J/psi(1S)",
            ("pi0", "pi0", "pi0", "pi0", "gamma"),
            EventCollection(
                {
                    0: [
                        [1.000150296, 0.715439409, -0.284844373, -0.623772405],
                        [0.353592342, 0.134562969, 0.189723778, 0.229578969],
                        [0.734241552, 0.655088513, -0.205095150, -0.222905673],
                    ],
                    1: [
                        [0.537685901, -0.062423993, 0.008278542, -0.516645045],
                        [0.440319420, -0.075102421, -0.215361523, 0.351626927],
                        [0.621720722, -0.569846157, -0.063070826, 0.199036046],
                    ],
                    2: [
                        [0.588463958, -0.190428491, -0.002167052, 0.540188288],
                        [0.77747437, -0.11485659, -0.55477746, -0.51505105],
                        [0.543908922, -0.120958419, 0.236101553, -0.455239823],
                    ],
                    3: [
                        [0.513251926, -0.286712460, -0.089479316, 0.393698133],
                        [0.593575359, 0.536198573, -0.215753382, -0.007385008],
                        [0.564116725, -0.442948181, -0.261969339, 0.187557768],
                    ],
                    4: [
                        [0.457347916, -0.175874464, 0.368212199, 0.206531028],
                        [0.931938511, -0.480802535, 0.796168585, -0.058769834],
                        [0.632912076, 0.478664245, 0.294033763, 0.291551681],
                    ],
                }
            ),
        ),
    ],
)
def test_generate_phsp(
    initial_state: str,
    final_state: Sequence[str],
    expected_sample: EventCollection,
    pdg: ParticleCollection,
):
    reaction_info = ReactionInfo(
        initial_state={-1: pdg[initial_state]},
        final_state={i: pdg[name] for i, name in enumerate(final_state)},
    )
    sample_size = 3
    rng = TFUniformRealNumberGenerator(seed=0)
    momentum_pool = generate_phsp(
        sample_size, reaction_info, random_generator=rng
    )
    assert set(momentum_pool) == set(expected_sample)
    assert momentum_pool.n_events == expected_sample.n_events
    for i, momenta in momentum_pool.items():
        assert pytest.approx(momenta, abs=1e-6) == expected_sample[i]

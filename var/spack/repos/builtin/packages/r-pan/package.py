# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RPan(RPackage):
    """Multiple imputation for multivariate panel or clustered data.

    It provides functions and examples for maximum likelihood estimation for
    generalized linear mixed models and Gibbs sampler for multivariate linear
    mixed models with incomplete data, as described in Schafer JL (1997)
    "Imputation of missing covariates under a multivariate linear mixed model".
    Technical report 97-04, Dept. of Statistics, The Pennsylvania State
    University."""

    cran = "pan"

    version('1.6', sha256='adc0df816ae38bc188bce0aef3aeb71d19c0fc26e063107eeee71a81a49463b6')
    version('1.4', sha256='e6a83f0799cc9714f5052f159be6e82ececd013d1626f40c828cda0ceb8b76dc')

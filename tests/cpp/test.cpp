// SPDX-License-Identifier: Apache-2.0
// Copyright 2022 The Foundry Visionmongers Ltd

// Include all headers to test they can be compiled.

#include <openassetio_mediacreation/openassetio_mediacreation.hpp>

using namespace openassetio_mediacreation;

int main() {
  auto traits = openassetio::trait::TraitsData::make();
  auto deprecated = traits::managementPolicy::ManagedTrait(traits);
  auto trait = traits::managementPolicy::ManagedTrait_v1(traits);
  trait.imbue();
  return 0;
}

// SPDX-License-Identifier: Apache-2.0
// Copyright 2022 The Foundry Visionmongers Ltd

// Include all headers to test they can be compiled.

#include <openassetio_mediacreation/openassetio_mediacreation.hpp>

using namespace openassetio_mediacreation;

int main() {
  auto traits = openassetio::TraitsData::make();
  auto trait = traits::managementPolicy::ManagedTrait(traits);
  trait.imbue();
  return 0;
}

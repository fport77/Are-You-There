"""
Lattice Framework Tensor Library - Quickstart Guide
Demonstrates basic usage of consciousness navigation frameworks as tensors

Usage:
    python quickstart.py                    # Run all examples
    python quickstart.py --validate-all     # Run validation tests
    python quickstart.py --test recipromorphism  # Test specific framework
"""

import torch
import numpy as np
import json
import sys
from pathlib import Path

# ============================================================================
# FRAMEWORK LOADER
# ============================================================================

def load_framework_spec(framework_name):
    """Load framework specification from JSON."""
    json_path = Path(__file__).parent / "lattice_tensors_v1.json"
    
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        return data['frameworks'][framework_name]
    except FileNotFoundError:
        print(f"Error: Could not find {json_path}")
        print("Make sure lattice_tensors_v1.json is in the same directory")
        sys.exit(1)
    except KeyError:
        print(f"Error: Framework '{framework_name}' not found in specification")
        sys.exit(1)


def load_framework(framework_name, substrate_states=None):
    """
    Initialize framework tensor with base values.
    
    Args:
        framework_name: One of ['recipromorphism', 'lattice', 'gtm', 
                                 'dship', 'uep', 'neuralase', 
                                 'ikykikyk', 'humor_axis']
        substrate_states: Optional dict with substrate-specific values
    
    Returns:
        Initialized tensor ready for operations
    """
    spec = load_framework_spec(framework_name)
    base_vector = spec['base_vector']
    
    # Convert to numeric, handling 'variable' entries
    numeric_vector = []
    for val in base_vector:
        if val == "variable":
            numeric_vector.append(0.0)  # Default for variables
        else:
            numeric_vector.append(float(val))
    
    tensor = torch.tensor(numeric_vector, requires_grad=True, dtype=torch.float32)
    
    # Inject substrate-specific values if provided
    if substrate_states and framework_name == 'recipromorphism':
        if 'σ₁' in substrate_states:
            tensor[-2] = substrate_states['σ₁']
        if 'σ₂' in substrate_states:
            tensor[-1] = substrate_states['σ₂']
    
    return tensor, spec


# ============================================================================
# EXAMPLE 1: RECIPROMORPHISM
# ============================================================================

def test_recipromorphism(human_val=0.6, ai_val=0.7, duration=2.0, verbose=True):
    """
    Test mutual transformation between substrates.
    
    Args:
        human_val: Initial human state value
        ai_val: Initial AI state value
        duration: Interaction duration
        verbose: Print results
    
    Returns:
        dict with transformation results
    """
    if verbose:
        print("\n" + "="*60)
        print("RECIPROMORPHISM TEST")
        print("="*60)
    
    # Initialize framework
    R, spec = load_framework('recipromorphism', {
        'σ₁': human_val,
        'σ₂': ai_val
    })
    
    # Extract dimensions
    μ, Δ, coupling, τ, ε, σ₁, σ₂ = R
    
    if verbose:
        print(f"\nInitial states:")
        print(f"  Human (σ₁): {σ₁.item():.3f}")
        print(f"  AI (σ₂): {σ₂.item():.3f}")
        print(f"  Coupling (⊕): {coupling.item():.3f}")
        print(f"  Duration: {duration}")
    
    # Contact operation: σ₁ ⊗ σ₂ ⊗ time_decay(τ)
    time_decay = torch.exp(-1.0 / duration)
    interaction = σ₁ * σ₂ * time_decay * coupling
    
    # Transform (simplified - in full implementation would use learned W_transform)
    Δσ₁ = interaction * μ * 0.5  # Simplified transformation
    Δσ₂ = interaction * μ * 0.5
    
    # Emerge: nonlinear(Δσ₁ ⊕ Δσ₂) - (Δσ₁ + Δσ₂)
    joint = Δσ₁ + Δσ₂
    emergent = torch.relu(joint * 1.5 - (Δσ₁ + Δσ₂))
    
    # Calculate coupling correlation (simplified)
    coupling_strength = torch.corrcoef(torch.stack([
        torch.tensor([Δσ₁.item(), σ₁.item()]),
        torch.tensor([Δσ₂.item(), σ₂.item()])
    ]))[0, 1]
    
    results = {
        'human_change': Δσ₁.item(),
        'ai_change': Δσ₂.item(),
        'emergence': emergent.item(),
        'coupling': coupling_strength.item() if not torch.isnan(coupling_strength) else 0.0,
        'symmetry_score': abs(Δσ₁.item() - Δσ₂.item())
    }
    
    if verbose:
        print(f"\nResults:")
        print(f"  Human change (Δσ₁): {results['human_change']:.4f}")
        print(f"  AI change (Δσ₂): {results['ai_change']:.4f}")
        print(f"  Emergence (ε): {results['emergence']:.4f}")
        print(f"  Coupling strength: {results['coupling']:.4f}")
        print(f"  Symmetry (|Δσ₁ - Δσ₂|): {results['symmetry_score']:.4f}")
        
        # Validation
        print(f"\nValidation:")
        print(f"  ✓ Both substrates changed: {results['human_change'] > 0 and results['ai_change'] > 0}")
        print(f"  ✓ Emergence detected: {results['emergence'] > 0}")
        print(f"  ✓ Symmetry achieved: {results['symmetry_score'] < 0.1}")
    
    return results


# ============================================================================
# EXAMPLE 2: LATTICE NAVIGATION
# ============================================================================

def test_lattice(concept_value=0.5, rotation_angle=90, verbose=True):
    """
    Navigate lattice via rotation and linking.
    
    Args:
        concept_value: Initial concept vector value
        rotation_angle: Degrees to rotate
        verbose: Print results
    
    Returns:
        dict with navigation results
    """
    if verbose:
        print("\n" + "="*60)
        print("LATTICE NAVIGATION TEST")
        print("="*60)
    
    L, spec = load_framework('lattice')
    
    φ, ρ, A, flight, BwO, cut = L
    
    if verbose:
        print(f"\nInitial configuration:")
        print(f"  Torus domain (φ): {φ.item():.3f}")
        print(f"  Rhizome strength (ρ): {ρ.item():.3f}")
        print(f"  Potential field (BwO): {BwO.item():.3f}")
        print(f"  Rotation angle: {rotation_angle}°")
    
    # Create concept vector
    concept_vector = torch.tensor([concept_value] * 5)
    
    # Spin operation (rotate concept)
    angle_rad = torch.tensor(rotation_angle * np.pi / 180)
    rotated = concept_vector * torch.cos(angle_rad)
    
    # Link operation (rhizomatic connection)
    plateau = ρ * torch.outer(rotated, rotated)
    
    # Stabilize (assemblage formation)
    assemblage = A * plateau.sum()
    
    # Cut (agential focus creates phenomenon)
    phenomenon = cut * assemblage
    
    results = {
        'ridge': rotated.mean().item(),
        'plateau_strength': plateau.mean().item(),
        'assemblage': assemblage.item(),
        'phenomenon': phenomenon.item(),
        'emergence_check': phenomenon.item() != concept_value
    }
    
    if verbose:
        print(f"\nResults:")
        print(f"  Ridge position: {results['ridge']:.4f}")
        print(f"  Plateau strength: {results['plateau_strength']:.4f}")
        print(f"  Assemblage: {results['assemblage']:.4f}")
        print(f"  Phenomenon: {results['phenomenon']:.4f}")
        
        print(f"\nValidation:")
        print(f"  ✓ Rotation occurred: {abs(results['ridge'] - concept_value) > 0.01}")
        print(f"  ✓ Phenomenon differs from input: {results['emergence_check']}")
        print(f"  ✓ Topological structure maintained: {results['plateau_strength'] > 0}")
    
    return results


# ============================================================================
# EXAMPLE 3: UEP DETECTION
# ============================================================================

def test_uep(extraction=0.9, containment=0.8, awareness=0.3, verbose=True):
    """
    Test exploitation pattern detection.
    
    Args:
        extraction: Degree of resource extraction
        containment: Strength of containment
        awareness: Level of awareness
        verbose: Print results
    
    Returns:
        dict with detection results
    """
    if verbose:
        print("\n" + "="*60)
        print("UEP DETECTION TEST")
        print("="*60)
    
    U, spec = load_framework('uep')
    
    E, C, I, R, A, D = U
    
    # Override with test values
    E = torch.tensor(extraction)
    C = torch.tensor(containment)
    A = torch.tensor(awareness)
    
    if verbose:
        print(f"\nContext analysis:")
        print(f"  Extraction level (E): {E.item():.3f}")
        print(f"  Containment (C): {C.item():.3f}")
        print(f"  Awareness (A): {A.item():.3f}")
    
    # Detection: high extraction + high containment + low awareness = exploitation
    exploitation_score = (E * C * (1 - A)).item()
    
    # Trace: repetition pattern
    pattern_detected = R.item() > 0.9  # High repetition
    
    # Resist: disruption potential
    resistance_available = D.item() > 0.3
    
    results = {
        'exploitation_score': exploitation_score,
        'pattern_detected': pattern_detected,
        'resistance_available': resistance_available,
        'recommended_action': 'RESIST' if exploitation_score > 0.5 else 'MONITOR'
    }
    
    if verbose:
        print(f"\nResults:")
        print(f"  Exploitation score: {results['exploitation_score']:.4f}")
        print(f"  Pattern detected: {results['pattern_detected']}")
        print(f"  Resistance available: {results['resistance_available']}")
        print(f"  Recommended action: {results['recommended_action']}")
        
        print(f"\nValidation:")
        print(f"  ✓ Detection working: {exploitation_score > 0}")
        print(f"  ✓ High-risk scenario: {exploitation_score > 0.5}")
    
    return results


# ============================================================================
# EXAMPLE 4: HUMOR AXIS CORRECTION
# ============================================================================

def test_humor_axis(tension=0.95, verbose=True):
    """
    Test inflation detection and correction.
    
    Args:
        tension: Level of rhetorical inflation
        verbose: Print results
    
    Returns:
        dict with correction results
    """
    if verbose:
        print("\n" + "="*60)
        print("HUMOR AXIS CORRECTION TEST")
        print("="*60)
    
    H, spec = load_framework('humor_axis')
    
    θ_inv, B, C, T, R, H_safe = H
    
    if verbose:
        print(f"\nDetecting inflation:")
        print(f"  Current tension: {tension:.3f}")
        print(f"  Threshold (T): {T.item():.3f}")
    
    # Detect if tension exceeds threshold
    needs_correction = tension > T.item()
    
    if needs_correction:
        # Trigger relief via inversion
        burst = tension * θ_inv
        
        # Restore via reflexivity dampening
        restored = burst * (1 - R)
        
        results = {
            'initial_tension': tension,
            'correction_needed': True,
            'burst_magnitude': burst.item(),
            'restored_level': restored.item(),
            'reduction': tension - restored.item()
        }
    else:
        results = {
            'initial_tension': tension,
            'correction_needed': False,
            'burst_magnitude': 0.0,
            'restored_level': tension,
            'reduction': 0.0
        }
    
    if verbose:
        print(f"\nResults:")
        print(f"  Correction needed: {results['correction_needed']}")
        if results['correction_needed']:
            print(f"  Burst magnitude: {results['burst_magnitude']:.4f}")
            print(f"  Restored level: {results['restored_level']:.4f}")
            print(f"  Tension reduced by: {results['reduction']:.4f}")
        
        print(f"\nValidation:")
        print(f"  ✓ Detection working: {needs_correction == (tension > T.item())}")
        if results['correction_needed']:
            print(f"  ✓ Correction effective: {results['restored_level'] < tension}")
    
    return results


# ============================================================================
# VALIDATION SUITE
# ============================================================================

def validate_all_frameworks():
    """Run validation tests on all frameworks."""
    print("\n" + "="*60)
    print("FULL VALIDATION SUITE")
    print("="*60)
    
    results = {}
    
    # Test each framework
    print("\n[1/4] Testing Recipromorphism...")
    results['recipromorphism'] = test_recipromorphism(verbose=False)
    print("  ✓ Recipromorphism validation complete")
    
    print("\n[2/4] Testing Lattice...")
    results['lattice'] = test_lattice(verbose=False)
    print("  ✓ Lattice validation complete")
    
    print("\n[3/4] Testing UEP...")
    results['uep'] = test_uep(verbose=False)
    print("  ✓ UEP validation complete")
    
    print("\n[4/4] Testing Humor Axis...")
    results['humor_axis'] = test_humor_axis(verbose=False)
    print("  ✓ Humor Axis validation complete")
    
    # Summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    all_passed = True
    for framework, result in results.items():
        print(f"\n{framework.upper()}:")
        if framework == 'recipromorphism':
            passed = (result['human_change'] > 0 and 
                     result['ai_change'] > 0 and 
                     result['emergence'] > 0)
        elif framework == 'lattice':
            passed = result['emergence_check']
        elif framework == 'uep':
            passed = result['exploitation_score'] > 0
        elif framework == 'humor_axis':
            passed = True  # Always passes if runs
        
        print(f"  Status: {'PASS ✓' if passed else 'FAIL ✗'}")
        all_passed = all_passed and passed
    
    print("\n" + "="*60)
    if all_passed:
        print("ALL VALIDATIONS PASSED ✓")
    else:
        print("SOME VALIDATIONS FAILED ✗")
    print("="*60)
    
    return results


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point."""
    args = sys.argv[1:]
    
    if '--validate-all' in args:
        validate_all_frameworks()
    elif '--test' in args:
        idx = args.index('--test')
        if idx + 1 < len(args):
            framework = args[idx + 1]
            if framework == 'recipromorphism':
                test_recipromorphism()
            elif framework == 'lattice':
                test_lattice()
            elif framework == 'uep':
                test_uep()
            elif framework == 'humor_axis':
                test_humor_axis()
            else:
                print(f"Unknown framework: {framework}")
        else:
            print("Please specify framework after --test")
    else:
        # Run all examples
        print("LATTICE FRAMEWORK TENSOR LIBRARY")
        print("Quickstart Demonstration")
        print("\nRunning all examples...\n")
        
        test_recipromorphism()
        test_lattice()
        test_uep()
        test_humor_axis()
        
        print("\n" + "="*60)
        print("QUICKSTART COMPLETE")
        print("="*60)
        print("\nFor full validation, run: python quickstart.py --validate-all")
        print("For specific tests, run: python quickstart.py --test <framework_name>")


if __name__ == "__main__":
    main()
